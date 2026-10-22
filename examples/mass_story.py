"""Mass-story narration pipeline (docs/audio-creators.md).

Writes scene blocks with an LLM and narrates each with a per-character voice.

Usage:
    export SECRETVOICE_API_KEY=...
    export VENICE_INFERENCE_KEY=...
    python examples/mass_story.py
"""

import os

# --- 1. LLM writes the story blocks (any OpenAI-compatible client) --------
from openai import OpenAI

llm = OpenAI(
    api_key=os.environ.get("VENICE_INFERENCE_KEY"),
    base_url="https://api.venice.ai/api/v1",
)

STORY = llm.chat.completions.create(
    model="olafangensan-glm-4.7-flash-heretic",
    messages=[
        {"role": "system", "content": (
            "Write a short romantic scene (6 lines) with speaker tags. "
            "Format: [NARRATOR], [HER], [HIM]. Keep it intimate, not explicit."
        )},
        {"role": "user", "content": "A rainy night, first confession."},
    ],
    temperature=0.8,
).choices[0].message.content

print("--- story ---\n", STORY)

# --- 2. Map each speaker to a voice ----------------------------------------
VOICES = {"NARRATOR": "professor", "HER": "velvet", "HIM": "blaze"}

from secretvoice.client import SecretVoiceClient

voice = SecretVoiceClient(api_key=os.environ.get("SECRETVOICE_API_KEY"))

for line in STORY.splitlines():
    line = line.strip()
    if not line:
        continue
    if "]" in line:
        speaker, _, text = line.partition("]")
        speaker = speaker.strip(" [")
        voice_id = VOICES.get(speaker, "professor")
    else:
        voice_id, text = "professor", line
    audio = voice.text_to_speech.convert(
        text=text.strip(), voice_id=voice_id, output_format="mp3_44100_128"
    )
    name = f"out/{speaker or 'narrator'}_{abs(hash(text)) % 1000}.mp3"
    os.makedirs("out", exist_ok=True)
    open(name, "wb").write(audio)
    print(f"narrated [{voice_id}]: {name}")

# --- 3. Assemble with ffmpeg:  ffmpeg -f concat -i list.txt out/chapter.mp3
print("done — concatenate out/*.mp3 with ffmpeg to build the chapter.")