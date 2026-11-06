# Multilingual AI Translator

A full-stack web application that provides AI-powered translation services from English to five major Indian languages: **Hindi**, **Kannada**, **Tamil**, **Telugu**, and **Malayalam**. The application supports multiple input modes including text, speech, and file uploads (audio/video).

## 💡 Why This Project?

### Problem Statement
India is a linguistically diverse country with 22 official languages and hundreds of dialects. While English serves as a common language for education, business, and technology, there's a significant language barrier for millions of people who are more comfortable with their native languages. This creates challenges in:
- **Education:** Accessing educational content primarily available in English
- **Digital Content:** Consuming online content, videos, and media
- **Communication:** Bridging gaps between English-speaking and regional language communities
- **Accessibility:** Making information available to non-English speakers

### Project Motivation
This project was developed to address the language barrier by creating an accessible, AI-powered translation system that:
1. **Democratizes Information Access:** Enables people to translate English content to their preferred Indian languages instantly
2. **Supports Multiple Input Modes:** Accommodates different user preferences - text input, voice recording, or file uploads
3. **Leverages State-of-the-Art AI:** Utilizes cutting-edge models (NLLB and Wav2Vec2) for accurate translations and transcriptions
4. **Provides Real-World Solutions:** Handles practical use cases like video subtitles, audio transcription, and document translation

### Key Objectives
- **Accessibility:** Make translation services easily accessible through a user-friendly web interface
- **Accuracy:** Use advanced AI models to ensure high-quality translations
- **Versatility:** Support multiple input formats (text, speech, audio/video files)
- **Performance:** Build a fast, responsive system that can handle real-time translation requests
- **Learning:** Gain hands-on experience with modern AI/ML technologies, full-stack development, and API integration

### Real-World Applications
- **Educational Institutions:** Translate course materials and lectures to regional languages
- **Content Creators:** Generate subtitles and translations for videos
- **Businesses:** Localize content for regional markets
- **Government Services:** Make public information accessible in multiple languages
- **Media & Entertainment:** Translate news, articles, and entertainment content

### Technical Learning Outcomes
This project provided valuable experience in:
- **AI/ML Integration:** Working with pre-trained models (NLLB, Wav2Vec2) from Hugging Face
- **Full-Stack Development:** Building REST APIs with FastAPI and modern React frontend
- **Audio/Video Processing:** Handling multimedia files with MoviePy and PyTorch Audio
- **API Design:** Creating well-structured, documented APIs with proper error handling
- **Modern Web Technologies:** Using React 19, Vite, Tailwind CSS, and Framer Motion
- **Production-Ready Code:** Implementing best practices in code organization, error handling, and user experience

### Impact & Future Scope
This project demonstrates how AI can be leveraged to solve real-world problems and bridge communication gaps. Future enhancements could include:
- Support for more languages (all 22 official Indian languages)
- Bidirectional translation (regional languages to English)
- Real-time translation during video playback
- Mobile application development
- Integration with popular platforms (YouTube, educational portals)

## 🎯 What Makes This Project Different?

### Comparison with Other Translation Projects

While there are many translation tools available (Google Translate, Microsoft Translator, etc.), this project offers several unique advantages:

#### 1. **Specialized Focus on Indian Languages**
- **Most translation tools** prioritize major world languages (Spanish, French, Chinese)
- **This project** specifically targets five major Indian languages with optimized NLLB model support
- Better understanding of Indian language nuances and cultural context

#### 2. **Integrated Speech-to-Text Pipeline**
- **Other projects** typically separate translation and transcription services
- **This project** provides a complete workflow: Speech → Text → Translation in one platform
- Uses state-of-the-art Wav2Vec2 model specifically trained for English transcription
- Seamless integration between audio processing and translation

#### 3. **Video File Processing Capability**
- **Most translation tools** only handle text or audio files
- **This project** can extract audio from video files and process them automatically
- Supports video formats (MP4, AVI, etc.) with automatic audio extraction using MoviePy
- Complete solution for content creators who need to translate video content

#### 4. **Self-Hosted & Open Architecture**
- **Commercial services** (Google Translate API, etc.) require API keys, usage limits, and ongoing costs
- **This project** runs entirely on your own infrastructure with no external API dependencies
- Full control over data privacy and processing
- No per-request costs or usage restrictions

#### 5. **Full-Stack Custom Implementation**
- **Many projects** are either frontend-only (using third-party APIs) or backend-only (no UI)
- **This project** is a complete full-stack application with custom-built frontend and backend
- Modern, responsive UI built with React 19 and Tailwind CSS
- RESTful API architecture with FastAPI for optimal performance

#### 6. **Multiple Input Modalities**
- **Traditional tools** typically support only one input method (text OR speech)
- **This project** supports three distinct modes:
  - Direct text input
  - Real-time microphone recording
  - File upload (audio/video)
- Flexible workflow for different user needs and scenarios

#### 7. **Academic Research & Learning Focus**
- **Commercial projects** focus on monetization and user acquisition
- **This project** emphasizes learning, research, and understanding AI/ML technologies
- Comprehensive documentation of the development process (16-week project diary)
- Educational value for understanding NLP, speech processing, and full-stack development

#### 8. **Modern Technology Stack**
- **Legacy projects** may use older frameworks and technologies
- **This project** uses cutting-edge technologies:
  - React 19 (latest version)
  - FastAPI (modern async Python framework)
  - NLLB-200 (Facebook's latest multilingual model)
  - Wav2Vec2 (state-of-the-art speech recognition)
- Built with performance and scalability in mind

#### 9. **End-to-End Workflow**
- **Fragmented solutions** require multiple tools (transcription tool + translation tool)
- **This project** provides a unified platform:
  - Upload video → Extract audio → Transcribe → Translate
  - All in one seamless workflow
- No need to switch between different applications

#### 10. **Privacy & Data Control**
- **Cloud-based services** send your data to external servers
- **This project** processes everything locally on your server
- No data leaves your infrastructure
- Ideal for sensitive content, educational institutions, or organizations with data privacy requirements

### Technical Differentiators

| Feature | This Project | Typical Translation Tools |
|---------|-------------|---------------------------|
| **Video Processing** | ✅ Native support | ❌ Not available |
| **Speech-to-Text** | ✅ Integrated Wav2Vec2 | ⚠️ Separate service required |
| **Self-Hosted** | ✅ Fully self-contained | ❌ Cloud API dependent |
| **Indian Languages** | ✅ Optimized support | ⚠️ Generic support |
| **Cost** | ✅ Free (self-hosted) | ⚠️ Pay-per-use API |
| **Data Privacy** | ✅ Local processing | ⚠️ Cloud processing |
| **Full-Stack** | ✅ Complete application | ⚠️ Usually API-only |
| **Open Source** | ✅ Customizable | ❌ Proprietary |

## ⚙️ How the Project Works

### System Architecture

The project follows a **client-server architecture** with a React frontend communicating with a FastAPI backend:

```
┌─────────────────┐         HTTP/REST API         ┌─────────────────┐
│                 │ ◄──────────────────────────► │                 │
│  React Frontend │                               │  FastAPI Backend│
│  (Port 5173)    │                               │  (Port 8000)    │
│                 │                               │                 │
└─────────────────┘                               └─────────────────┘
                                                          │
                                                          │
                                    ┌─────────────────────┼─────────────────────┐
                                    │                     │                     │
                                    ▼                     ▼                     ▼
                            ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
                            │  NLLB Model  │    │ Wav2Vec2     │    │   MoviePy    │
                            │  (Translation)│   │  (Speech-to- │    │  (Video      │
                            │              │    │   Text)       │    │   Processing)│
                            └──────────────┘    └──────────────┘    └──────────────┘
```

### Workflow Overview

#### 1. **Text Translation Workflow**

```
User Input (English Text)
    │
    ▼
React Frontend (TextTranslator.jsx)
    │
    ▼
POST /translate API Request
    │
    ├─► FastAPI Backend (main.py)
    │       │
    │       ▼
    │   Pydantic Validation
    │       │
    │       ▼
    │   translator.py → NLLB Model
    │       │
    │       ├─► Language Code Mapping
    │       │   (hi → hin_Deva, kn → kan_Knda, etc.)
    │       │
    │       ▼
    │   Translation Processing
    │       │
    │       ▼
    │   Return Translated Text
    │
    ▼
Display Translation in UI
```

**Step-by-Step:**
1. User enters English text and selects target language
2. Frontend sends POST request to `/translate` endpoint with JSON payload
3. FastAPI validates request using Pydantic models
4. Backend maps frontend language code to NLLB language code
5. NLLB model processes translation (English → Target Language)
6. Translated text is returned as JSON response
7. Frontend displays the translation to the user

#### 2. **Speech Translation Workflow**

```
User Records Audio (Microphone)
    │
    ▼
React Frontend (SpeechTranslator.jsx)
    │
    ├─► MediaRecorder API captures audio
    │
    ▼
Convert to Audio Blob/File
    │
    ▼
POST /stt API Request (Multipart Form Data)
    │
    ├─► FastAPI Backend (main.py)
    │       │
    │       ▼
    │   Receive Audio File
    │       │
    │       ▼
    │   PyTorch Audio Processing
    │       ├─► Load audio file
    │       ├─► Resample to 16kHz (if needed)
    │       └─► Convert to mono channel
    │       │
    │       ▼
    │   Wav2Vec2 Model Processing
    │       ├─► Preprocess audio with Wav2Vec2Processor
    │       ├─► Generate logits (model predictions)
    │       ├─► Decode to text (CTC decoding)
    │       └─► Return English transcription
    │
    ▼
Display Transcription
    │
    ▼
User can then translate transcribed text
    │
    ▼
Follow Text Translation Workflow
```

**Step-by-Step:**
1. User clicks "Start Recording" → Browser requests microphone permission
2. MediaRecorder API captures audio in real-time
3. User clicks "Stop Recording" → Audio blob is created
4. Frontend sends audio file to `/stt` endpoint
5. Backend loads audio using PyTorch Audio
6. Audio is preprocessed (resampled to 16kHz, converted to mono)
7. Wav2Vec2 model processes audio → generates transcription
8. English text is returned to frontend
9. User can then translate the transcribed text using the translation workflow

#### 3. **File Upload Translation Workflow**

```
User Uploads Audio/Video File
    │
    ▼
React Frontend (UploadTranslator.jsx)
    │
    ├─► Drag & Drop or File Selection
    │
    ▼
File Validation (Format Check)
    │
    ▼
POST /stt API Request (File Upload)
    │
    ├─► FastAPI Backend (main.py)
    │       │
    │       ▼
    │   Check File Type
    │       │
    │       ├─► If Video File:
    │       │       │
    │       │       ▼
    │       │   MoviePy Processing
    │       │       ├─► Load video file
    │       │       ├─► Extract audio track
    │       │       └─► Convert to audio format
    │       │
    │       └─► If Audio File:
    │               │
    │               ▼
    │           Direct Processing
    │
    │       ▼
    │   PyTorch Audio Processing
    │       ├─► Load audio
    │       ├─► Resample to 16kHz
    │       └─► Convert to mono
    │       │
    │       ▼
    │   Wav2Vec2 Model Processing
    │       ├─► Transcribe audio
    │       └─► Return English text
    │
    ▼
Display Transcription
    │
    ▼
User selects target language
    │
    ▼
Follow Text Translation Workflow
```

**Step-by-Step:**
1. User uploads audio or video file (drag & drop or file picker)
2. Frontend validates file format
3. File is sent to `/stt` endpoint via multipart form data
4. Backend checks content type:
   - **If video:** MoviePy extracts audio track
   - **If audio:** Direct processing
5. Audio is processed (resampled, converted to mono)
6. Wav2Vec2 transcribes audio to English text
7. Transcription is displayed in UI
8. User selects target language and translates

### Technical Components

#### Backend Components

1. **FastAPI Application (`main.py`)**
   - Handles HTTP requests and routing
   - Manages CORS for frontend communication
   - Validates requests using Pydantic models
   - Coordinates between different services

2. **Translation Module (`translator.py`)**
   - Loads NLLB model on startup
   - Maps language codes (frontend → NLLB format)
   - Processes translation requests
   - Returns translated text

3. **Speech-to-Text Processing (`main.py` - `/stt` endpoint)**
   - Receives audio/video files
   - Handles video-to-audio conversion (MoviePy)
   - Preprocesses audio (PyTorch Audio)
   - Runs Wav2Vec2 inference
   - Returns transcribed text

#### Frontend Components

1. **TextTranslator Component**
   - Text input field
   - Language selection dropdown
   - API integration for translation
   - Result display with copy functionality

2. **SpeechTranslator Component**
   - Microphone access handling
   - MediaRecorder API integration
   - Real-time recording controls
   - Audio file upload to backend

3. **UploadTranslator Component**
   - File upload interface (drag & drop)
   - File validation
   - Progress indicators
   - Transcription and translation display

### Data Flow

```
┌──────────────┐
│   User       │
│   Input      │
└──────┬───────┘
       │
       ▼
┌──────────────┐      HTTP Request      ┌──────────────┐
│   React      │ ────────────────────► │   FastAPI    │
│   Frontend   │                        │   Backend    │
└──────────────┘                        └──────┬───────┘
       ▲                                        │
       │                                        ▼
       │                                ┌──────────────┐
       │                                │   AI Models  │
       │                                │  (NLLB/      │
       │                                │  Wav2Vec2)   │
       │                                └──────┬───────┘
       │                                        │
       │                                        ▼
       │                                ┌──────────────┐
       │                                │  Processing  │
       │                                │  & Inference│
       │                                └──────┬───────┘
       │                                        │
       │                                        ▼
       │                                ┌──────────────┐
       │                                │   Response   │
       │                                │   (JSON)     │
       │                                └──────┬───────┘
       │                                        │
       │      HTTP Response                      │
       └─────────────────────────────────────────┘
```

### Model Loading & Initialization

**On Backend Startup:**
1. FastAPI application starts
2. NLLB model loads from Hugging Face (first time downloads ~600MB)
3. Wav2Vec2 model loads from Hugging Face (first time downloads ~1.3GB)
4. Models are cached in memory for fast inference
5. Server is ready to accept requests

**Note:** First request may be slower due to model initialization, subsequent requests are fast.

### Error Handling

- **Frontend:** Validates user input, handles API errors, shows user-friendly messages
- **Backend:** Validates requests, handles file processing errors, returns appropriate error responses
- **Model Errors:** Handles model loading failures, inference errors, and timeout scenarios

## 🌟 Features

### Three Translation Modes

1. **Text Translator**
   - Direct text input for instant translation
   - Support for all five target languages
   - Copy-to-clipboard functionality

2. **Speech Translator**
   - Real-time microphone recording
   - Speech-to-text conversion using Wav2Vec2
   - Automatic transcription and translation

3. **Upload Translator**
   - Upload audio or video files
   - Automatic audio extraction from videos
   - Complete workflow: Upload → Transcribe → Translate

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **NLLB (No Language Left Behind)** - Facebook's multilingual translation model
- **Wav2Vec2** - Facebook's speech-to-text model for English transcription
- **MoviePy** - Video processing and audio extraction
- **PyTorch** - Deep learning framework
- **Transformers (Hugging Face)** - Pre-trained model integration

### Frontend
- **React 19** - Modern UI library
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library for smooth transitions
- **React Router** - Client-side routing

## 📋 Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **pip** (Python package manager)
- **npm** or **yarn** (Node package manager)

## 🚀 Installation & Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd multilingual-ai-be
```

2. Create a virtual environment (recommended):
```bash
python -m venv env
```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     env\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source env/bin/activate
     ```

4. Install dependencies:
```bash
pip install fastapi uvicorn transformers torch torchaudio moviepy pydantic
```

5. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend API will be available at `http://localhost:8000`

**Note:** On first run, the models (NLLB and Wav2Vec2) will be downloaded automatically from Hugging Face. This may take several minutes depending on your internet connection.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd multilingual-ai-fe
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 📡 API Endpoints

### `GET /`
Health check endpoint
- **Response:** `{"message": "✅ NLLB Translation + English STT API is running"}`

### `POST /translate`
Translate English text to target language
- **Request Body:**
  ```json
  {
    "text": "Hello, how are you?",
    "target_lang": "hi"  // Options: "hi", "kn", "ta", "te", "ml"
  }
  ```
- **Response:**
  ```json
  {
    "input": "Hello, how are you?",
    "translation": "नमस्ते, आप कैसे हैं?"
  }
  ```

### `POST /stt`
Speech-to-text conversion for audio/video files
- **Request:** Multipart form data with file upload
- **Supported Formats:** Audio (wav, mp3, etc.) and Video (mp4, avi, etc.)
- **Response:**
  ```json
  {
    "text": "Transcribed English text from audio/video"
  }
  ```

## 🌐 Supported Languages

| Language | Code | NLLB Code |
|----------|------|-----------|
| Hindi | `hi` | `hin_Deva` |
| Kannada | `kn` | `kan_Knda` |
| Tamil | `ta` | `tam_Taml` |
| Telugu | `te` | `tel_Telu` |
| Malayalam | `ml` | `mal_Mlym` |

## 📁 Project Structure

```
multilingual-ai/
├── multilingual-ai-be/          # Backend (FastAPI)
│   ├── main.py                   # FastAPI application & routes
│   ├── translator.py             # NLLB translation module
│   └── env/                      # Virtual environment
│
├── multilingual-ai-fe/           # Frontend (React + Vite)
│   ├── src/
│   │   ├── components/           # Reusable components
│   │   │   ├── Navbar.jsx
│   │   │   └── Footer.jsx
│   │   ├── pages/                # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Contact.jsx
│   │   │   ├── TextTranslator.jsx
│   │   │   ├── SpeechTranslator.jsx
│   │   │   └── UploadTranslator.jsx
│   │   ├── App.jsx               # Main app component
│   │   └── main.jsx              # Entry point
│   ├── package.json
│   └── vite.config.js
│
└── Project_Diary_16_Weeks.md     # Development diary
```

## 🎯 Usage

### Text Translation
1. Navigate to the Text Translator page
2. Enter English text in the input field
3. Select target language from dropdown
4. Click "Translate" button
5. View translated text and copy if needed

### Speech Translation
1. Navigate to the Speech Translator page
2. Click "Start Recording" to begin audio capture
3. Speak in English
4. Click "Stop Recording" when done
5. The audio will be transcribed and can be translated

### File Upload Translation
1. Navigate to the Upload Translator page
2. Drag and drop or select an audio/video file
3. Wait for transcription to complete
4. Select target language and translate
5. Download transcribed/translated text if needed

## 🔧 Configuration

### CORS Settings
The backend CORS is configured to allow requests from `http://localhost:5173`. To change this, modify the `allow_origins` in `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Model Configuration
- **Translation Model:** `facebook/nllb-200-distilled-600M`
- **Speech-to-Text Model:** `facebook/wav2vec2-large-960h`
- Models are loaded on server startup and cached in memory

## 🐛 Troubleshooting

### Backend Issues
- **Model download fails:** Ensure stable internet connection. Models are large (~600MB+)
- **Memory errors:** Large video files may cause memory issues. Consider processing smaller chunks
- **Audio processing errors:** Ensure audio files are in supported formats

### Frontend Issues
- **CORS errors:** Verify backend CORS settings match frontend URL
- **API connection fails:** Ensure backend is running on port 8000
- **Microphone not working:** Check browser permissions for microphone access

## 📝 Development Notes

- The project was developed over 16 weeks as part of academic research
- Total development time: ~155 hours
- Models are loaded once at startup for optimal performance
- First API call may be slower due to model initialization

## 🤝 Contributing

This is an academic project, but suggestions and improvements are welcome!

## 📄 License

This project is developed for academic purposes under the guidance of Dr. Vinod Kumar P.

## 🙏 Acknowledgments

- **Facebook Research** - For NLLB and Wav2Vec2 models
- **Hugging Face** - For model hosting and transformers library
- **FastAPI** - For the excellent web framework
- **React Team** - For the powerful UI library

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [NLLB Model](https://huggingface.co/facebook/nllb-200-distilled-600M)
- [Wav2Vec2 Model](https://huggingface.co/facebook/wav2vec2-large-960h)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

---

**Project:** Multilingual AI Translator  
**Developer:** [Your Name]  
**Supervisor:** Dr. Vinod Kumar P
