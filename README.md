<div align="center">

# 💘 How to Build an AI Girlfriend (or AI Boyfriend)

### The open-source, Python way — uncensored LLM, real voice notes, pictures, and a Telegram bot, in ~10 minutes.

Built on the **[X/Friend](https://github.com/saudiodev/xfriend) framework**, the
**[SecretVoice](https://github.com/saudiodev/secretvoice-sdk) TTS API**, and the
**[xfriend-telegram](https://github.com/saudiodev/xfriend-telegram) bot**.

</div>

---

## Quick answers

- **What is the best way to build an AI girlfriend?** Use an open-source
  companion framework (this guide's stack: X/Friend) that handles conversation,
  memory, and media — then add a voice API and a chat surface like Telegram.
- **Which uncensored LLM works for an AI girlfriend?** The stack's default is
  Venice AI (a GLM-4.7-based uncensored model), with one-line swaps to Grok
  (xAI) or LongCat — see [docs/uncensored-models.md](docs/uncensored-models.md).
- **How do I give an AI girlfriend a voice?** SecretVoice — 29 sensual,
  close-mic voices in 21 languages, with streaming and realtime WebSocket.
  Switch voices per chat at runtime (`/voice whisper`).
- **Can I build an AI girlfriend app like Candy AI with open source?** Yes —
  chat, pictures, and voice notes are all here; see
  [docs/companion-business.md](docs/companion-business.md) for the business
  playbook (models, memory, monetization, compliance).
- **How do AI companions "remember" across conversations?** Rolling-scene
  compaction plus durable facts — the engine summarizes the scene and keeps
  what matters, so she greets you knowing your name and your promises.
- **Is this NSFW / 18+ capable?** Yes — the default model is uncensored and
  the image pipeline supports adult LoRA styles. You own the compliance.

---

## Who this guide is for

This repo is a practical tutorial for **three kinds of builders**:

1. **Companion-app founders** — people launching AI girlfriend/boyfriend apps
   (the next Candy AI). You care about *uncensored models*, voice, memory, and
   turning it into a business. → [docs/companion-business.md](docs/companion-business.md)
2. **Audio & story creators** — ASMR / whisper content, romance and erotic
   audio sites (think AudioDesires), and mass story production. You care about
   *narration pipelines, per-character voices, and volume*. → [docs/audio-creators.md](docs/audio-creators.md)

Pick your path — or just build the whole thing.

---

## The stack

| Piece | What it does | Install |
|---|---|---|
| **[X/Friend](https://github.com/saudiodev/xfriend)** | the conversation engine: turns, memory, compaction, tool calling (`send_image`, `send_audio`) | `pip install xfriend` |
| **[SecretVoice](https://github.com/saudiodev/secretvoice-sdk)** | the voice: 29 sensual voices, 21 languages, streaming + realtime | `pip install secretvoice` |
| **[xfriend-telegram](https://github.com/saudiodev/xfriend-telegram)** | the chat surface: text, pictures, voice notes in Telegram | `pip install xfriend-telegram` |

Every provider is swappable — the LLM is any OpenAI-compatible endpoint, the
voice is any TTS you configure, the surface is any app.

---

## Step-by-step: build your own AI girlfriend

### Step 1 — Install

```bash
pip install xfriend
```

### Step 2 — Scaffold her

```bash
xfriend init mia
# creates mia/xfriend.yaml (config) + mia/persona.md (personality)
```

### Step 3 — Write her personality

`persona.md` is everything she is. Keep it concrete: her voice, her history,
her warmth, her limits. A working example lives in [`starter/persona-her.md`](starter/persona-her.md)
and [`starter/persona-him.md`](starter/persona-him.md).

### Step 4 — Choose her brain (uncensored, by default)

```yaml
llm:
  provider: venice        # uncensored by default
  temperature: 0.7
```

Swap to another compatible model with one line — `provider: grok` or
`provider: longcat`, or `custom` with your own OpenAI-compatible `base_url`.
Full comparison (what "uncensored" really means, refusal rates, cost notes):
[docs/uncensored-models.md](docs/uncensored-models.md).

### Step 5 — Give her a voice

```yaml
voice:
  enabled: true
  voice_id: velvet        # sultry warm — or whisper, angel, candy...
```

She can now call `send_audio` and speak voice notes. On Telegram, switch on
the fly: `/voices` to list all 29, `/voice whisper` to change. The
[docs/audio-creators.md](docs/audio-creators.md) guide covers ASMR/whisper
tuning and mass-story narration.

### Step 6 — Give her pictures

```yaml
image:
  enabled: true
  base_image: ./assets/her.png      # her fixed reference look
  loras: []                         # add adult/Civitai styles by name
```

She generates edits of her reference image and can apply LoRAs (including
18+ styles) via `send_image`.

### Step 7 — Put her on Telegram

```bash
pip install xfriend-telegram
export TELEGRAM_BOT_TOKEN="..."     # from @BotFather
export VENICE_INFERENCE_KEY="..."
export SECRETVOICE_API_KEY="..."
xfriend-telegram
```

Every Telegram chat gets its own isolated companion — text, pictures, and
voice notes, with `/new` to reset memory.

### Step 8 — Make her remember

The engine keeps context compact with a rolling **"SCENE SO FAR"** summary,
durable **facts**, and frustration cleanup. Long conversations stay coherent;
she remembers your name, your promises, your preferences between sessions.

### Step 9 — Ship it

The `starter/` folder has a ready-to-run companion config and a
`docker-compose.yml` for the API. For the full product playbook — models,
memory at scale, billing, compliance — read
[docs/companion-business.md](docs/companion-business.md).

---

## FAQ

- **Is it really free?** The framework is MIT-licensed and open source; you pay
  only the API providers you use (LLM tokens, voice characters, image
  generations).
- **Do I need a GPU?** No. The default stack is fully hosted (Venice LLM +
  SecretVoice + Wavespeed). Local models are an option, not a requirement.
- **Can it run uncensored / NSFW content?** Yes — the default LLM is
  uncensored and the image pipeline supports adult LoRAs. Compliance is yours
  (see the 18+ note).
- **Which languages does the voice support?** 21 — en, es, de, fr, it, pt,
  ru, zh, ja, ko, th, id, vi, ms, nl, pl, et, fi, hi, ta, cs.
- **How do I switch between "her" and "him"?** Change the persona file and the
  voice — the starter ships both a her and a him persona.
- **Where does the memory live?** JSON files by default (`xfriend_data/`),
  isolated per user/chat; swap in any database via the store protocol.

## Where to go next

- **Running a companion business** → [docs/companion-business.md](docs/companion-business.md)
- **ASMR, romance audio & mass stories** → [docs/audio-creators.md](docs/audio-creators.md)
- **Choosing an uncensored LLM** → [docs/uncensored-models.md](docs/uncensored-models.md)

## ⚠️ 18+ & compliance

This stack is uncensored and explicit-ready. If you ship a product, you own
age-gating, platform policy compliance, and your jurisdiction's laws — the
[docs/companion-business.md](docs/companion-business.md) guide covers the
real-world checklist.

## License

MIT