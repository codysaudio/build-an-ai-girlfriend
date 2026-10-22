"""Give your companion a voice (README Step 5) and switch it at runtime.

Usage:  export SECRETVOICE_API_KEY=...  &&  python examples/voice_switch.py
"""

import os

from secretvoice.client import SecretVoiceClient
from secretvoice.play import play

client = SecretVoiceClient(api_key=os.environ.get("SECRETVOICE_API_KEY"))

print("All 29 voices:")
for v in client.voices.list():
    gender = v.labels.get("gender", "?")
    print(f"  {v.voice_id:12s} [{gender}] {v.name}")

audio = client.text_to_speech.convert(
    text="Hey you. I saved a spot for you right here. What are you waiting for?",
    voice_id="velvet",
    voice_settings={"stability": 0.4, "similarity_boost": 0.7, "style": 0.5, "speed": 0.95},
)
play(audio)