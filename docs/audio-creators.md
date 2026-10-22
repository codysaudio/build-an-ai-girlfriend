# Romantic Audio, ASMR & Mass-Story Production

For creators building whisper/ASMR content, romance and erotic audio sites
(the AudioDesires end of the market), and anyone producing **stories at
volume**: SecretVoice + an LLM give you a full narration pipeline.

## The 29 voices, tuned for closeness

SecretVoice ships 13 female + 16 male voices built for intimate audio —
breathy whispers, close-mic delivery, and micro-inflections that survive in
soft speech:

- **her:** velvet (sultry, unhurried), whisper (intimate, close-mic), angel
  (soft, delicate), candy, jade, chloe, honey, crystal, diamond, sunny, star...
- **him:** professor (measured warmth), titan (deep, commanding), blaze
  (passionate), phoenix, duke, rico, steele, sage, rex, maverick, tender...

Switch voice per scene with a config change — or per character in a story.

## ASMR / whisper presets

Whispered ASMR needs stability and a close-mic feel. A good starting point:

```python
audio = client.text_to_speech.convert(
    text="Come closer. I want to tell you a secret.",
    voice_id="whisper",
    voice_settings={
        "stability": 0.4,   # keep the breathy texture stable
        "similarity_boost": 0.7,
        "style": 0.5,       # expressiveness
        "speed": 0.9,       # unhurried
    },
)
```

Tune `style` up for performance reads, `speed` down for intimate whispers.

## Mass-story production: the pipeline

Produce chapters or shorts at scale:

1. **LLM writes the scene** — X/Friend or any OpenAI-compatible call with a
   "write chapter N of a romance serial" prompt.
2. **Voice mapping** — assign per-character voices (her = velvet, him = blaze,
   narrator = professor). Dialogue-to-voice mapping by speaker tag.
3. **Narrate** — one SecretVoice call per block, saved as chapter audio.
4. **Assemble** — stitch with ffmpeg, add cover art, publish.

A runnable script lives in [`examples/mass_story.py`](../examples/mass_story.py).

## Real-time storytelling agents

SecretVoice's **realtime WebSocket** streams audio frames live — an AI
storyteller who narrates interactively, or a live roleplay agent that never
breaks character:

```python
async for frame in client.text_to_speech.realtime(
    text=["The door creaks open... ", "and she whispers your name."],
    voice_id="whisper",
):
    ...  # frames ready for WebRTC / your player
```

## Building an AudioDesires-style site

The shape is simple and proven:

- **Library** of narrated stories, organized by category/tags.
- **Free preview + paid full access** — the preview is the first 30 seconds
  of each chapter; payment unlocks the rest.
- **Credit or subscription metering** — reuse the character-count model.
- **Search & discovery** — chapters, voices, and categories as filterable
  metadata.

The same pipeline serves audiobook-style romance serials, ASMR channels, and
interactive story apps.

## From this guide to production

- Try the voices in the [SecretVoice SDK README](https://github.com/saudiodev/secretvoice-sdk) (playable clips).
- Steal the starter config in [`../starter/`](../starter/) for a companion
  that narrates, not just chats.