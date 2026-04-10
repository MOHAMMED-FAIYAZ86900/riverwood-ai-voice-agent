import os
import tempfile
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from playsound import playsound

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# replace this with voice ID from check_voices.py
VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"

def speak_text(text):
    text = text[:300]

    audio_stream = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id="eleven_multilingual_v2",
        text=text
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        for chunk in audio_stream:
            f.write(chunk)
        path = f.name

    playsound(path)