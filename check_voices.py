import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

voices = client.voices.get_all()

for v in voices.voices:
    print("Voice Name:", v.name)
    print("Voice ID:", v.voice_id)
    print("-----")