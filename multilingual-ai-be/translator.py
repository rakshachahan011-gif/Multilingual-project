# translator.py
from transformers import pipeline
import torch

# Load NLLB model (first time it downloads weights)
print("Loading NLLB translation model...")
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    device=-1  # -1 = CPU, 0 = GPU
)
print("NLLB model loaded.")

def translate_text(text: str, target_lang: str) -> str:
    # Map frontend codes to NLLB codes
    language_mapping = {
        "kn": "kan_Knda", "te": "tel_Telu", "ta": "tam_Taml",
        "ml": "mal_Mlym", "hi": "hin_Deva",
    }
    nllb_target_code = language_mapping.get(target_lang)
    if not nllb_target_code:
        raise ValueError("Invalid target language selected.")
    
    # The pipeline is called with the source (always English) and target languages
    result = translator(text, src_lang="eng_Latn", tgt_lang=nllb_target_code, max_length=200)
    return result[0]['translation_text']