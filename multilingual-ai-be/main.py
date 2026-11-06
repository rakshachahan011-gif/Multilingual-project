# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from translator import translate_text  # existing translation module

import torch
import torchaudio
import io
import os
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from moviepy import AudioFileClip

# ------------------------
# File Size & Duration Limits
# ------------------------
MAX_AUDIO_SIZE_MB = 100  # Maximum audio file size in MB
MAX_VIDEO_SIZE_MB = 200   # Maximum video file size in MB
MAX_AUDIO_DURATION_MIN = 10  # Maximum audio duration in minutes
MAX_VIDEO_DURATION_MIN = 15  # Maximum video duration in minutes

MAX_AUDIO_SIZE_BYTES = MAX_AUDIO_SIZE_MB * 1024 * 1024
MAX_VIDEO_SIZE_BYTES = MAX_VIDEO_SIZE_MB * 1024 * 1024

# ------------------------
# Setup
# ------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# Models
# ------------------------
class TranslationRequest(BaseModel):
    text: str
    target_lang: str  # e.g., "kn", "te", "ta", "ml", "hi"

# ------------------------
# Load Wav2Vec2 English model
# ------------------------
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

# ------------------------
# Routes
# ------------------------
@app.get("/")
def home():
    return {
        "message": "✅ NLLB Translation + English STT API is running",
        "limits": {
            "audio": {
                "max_size_mb": MAX_AUDIO_SIZE_MB,
                "max_duration_minutes": MAX_AUDIO_DURATION_MIN
            },
            "video": {
                "max_size_mb": MAX_VIDEO_SIZE_MB,
                "max_duration_minutes": MAX_VIDEO_DURATION_MIN
            }
        }
    }

@app.post("/translate")
def handle_translation(req: TranslationRequest):
    try:
        translated_output = translate_text(req.text, req.target_lang)
        return {"input": req.text, "translation": translated_output}
    except ValueError as e:
        return {"error": str(e)}

@app.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    """
    Accepts audio or video file, returns English transcription
    
    Limits:
    - Audio files: Max 100 MB, Max 10 minutes
    - Video files: Max 200 MB, Max 15 minutes
    """
    try:
        # Read file in chunks to check size before full load
        file_size = 0
        chunks = []
        async for chunk in file.stream():
            chunks.append(chunk)
            file_size += len(chunk)
            
            # Check size limit early
            if file.content_type.startswith("video/"):
                if file_size > MAX_VIDEO_SIZE_BYTES:
                    raise HTTPException(
                        status_code=413,
                        detail=f"Video file too large. Maximum size: {MAX_VIDEO_SIZE_MB} MB"
                    )
            else:
                if file_size > MAX_AUDIO_SIZE_BYTES:
                    raise HTTPException(
                        status_code=413,
                        detail=f"Audio file too large. Maximum size: {MAX_AUDIO_SIZE_MB} MB"
                    )
        
        # Combine chunks
        audio_bytes = b''.join(chunks)
        
        # Check duration for video files
        if file.content_type.startswith("video/"):
            try:
                # Load video to check duration
                video_clip = AudioFileClip(io.BytesIO(audio_bytes))
                duration_seconds = video_clip.duration
                duration_minutes = duration_seconds / 60
                
                if duration_minutes > MAX_VIDEO_DURATION_MIN:
                    video_clip.close()
                    raise HTTPException(
                        status_code=413,
                        detail=f"Video too long. Maximum duration: {MAX_VIDEO_DURATION_MIN} minutes ({duration_minutes:.1f} minutes provided)"
                    )
                
                # Extract audio
                audio_clip = io.BytesIO()
                video_clip.audio.write_audiofile(audio_clip, codec="pcm_s16le")
                audio_clip.seek(0)
                waveform, sample_rate = torchaudio.load(audio_clip)
                video_clip.close()
            except HTTPException:
                raise
            except Exception as e:
                if "too long" in str(e).lower() or "duration" in str(e).lower():
                    raise HTTPException(
                        status_code=413,
                        detail=f"Video too long. Maximum duration: {MAX_VIDEO_DURATION_MIN} minutes"
                    )
                raise
        else:
            # Audio file - load and check duration
            waveform, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))
            duration_seconds = waveform.shape[1] / sample_rate
            duration_minutes = duration_seconds / 60
            
            if duration_minutes > MAX_AUDIO_DURATION_MIN:
                raise HTTPException(
                    status_code=413,
                    detail=f"Audio too long. Maximum duration: {MAX_AUDIO_DURATION_MIN} minutes ({duration_minutes:.1f} minutes provided)"
                )

        # Resample to 16kHz if needed
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)

        # Convert to mono
        if waveform.shape[0] > 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)

        # Run Wav2Vec2
        input_values = processor(waveform.squeeze().numpy(), return_tensors="pt", sampling_rate=16000).input_values
        with torch.no_grad():
            logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.decode(predicted_ids[0])

        return {"text": transcription}

    except HTTPException:
        # Re-raise HTTP exceptions (size/duration limits)
        raise
    except Exception as e:
        return {"error": str(e)}
