# Choosing an Uncensored LLM for Your AI Companion

The question founders ask most: *"which uncensored LLM can I actually build on?"*
Here's the straight answer, with a comparison you can quote.

## What "uncensored" actually means

Most hosted LLMs refuse intimate or explicit content at the API level. An
"uncensored" model has the refusal reflex tuned down or removed — it will
follow the scene you describe without moralizing, refusing, or rewriting your
content. It does **not** mean the model is unmoderated at the platform level:
age-gating and compliance are still your job.

## The comparison

| Provider | Default model | Censorship | Running it | Swap in X/Friend |
|---|---|---|---|---|
| **Venice AI** | `olafangensan-glm-4.7-flash-heretic` (GLM-4.7 based) | Uncensored, API-hosted, no GPU needed | Hosted API | `provider: venice` (the default) |
| **Grok (xAI)** | `grok-3` family | Lax — allows adult themes | Hosted API | `provider: grok` |
| **LongCat** | `LongCat-2.5-Preview` | Companion-tuned | Hosted API | `provider: longcat` |
| **Local models** (e.g. Gemma/Qwen/NemoMix variants, SillyTavern ecosystem) | varies | Uncensored | You run the GPU | `provider: custom` with your own endpoint |

### Hosted vs local — the trade-off

- **Hosted (Venice / Grok / LongCat):** zero GPU, instant, scales, but you
  trust the provider with conversations and pay per token.
- **Local:** total privacy, no per-token cost, but you need a decent GPU and
  you maintain the model yourself. The `custom` provider lets you point X/Friend
  at any OpenAI-compatible local server (vLLM, llama.cpp, etc.).

## Why Venice is the default here

- **Uncensored out of the box** — no prompt gymnastics, no refusal spirals.
- **GLM-4.7 class intelligence** at a flash price point.
- **Prompt-cache friendly** — the framework keeps your persona byte-stable,
  so long conversations stay fast and cheap.
- **OpenAI-compatible** — the same SDK works for every provider in the table.

## How to swap

```yaml
llm:
  provider: grok          # one line, same SDK
  # model: grok-3
```

Or bring your own:

```yaml
llm:
  provider: custom
  base_url: http://localhost:8000/v1
  model: my-uncensored-qlora
  api_key: not-needed
```

## Cost reality check

You pay per token for the LLM and per character of speech for the voice.
Companion conversations are short-turn and low-token; with prompt caching and
compaction (the framework rolls up old context instead of re-sending it), per
daily-active-user cost is small. Measure it yourself with the API dashboards —
don't trust the marketing.

## Compliance note

Uncensored ≠ unregulated. Ship age-gating, keep logs you can defend, and
follow your payment processor's and platform's adult-content policies. The
full checklist is in [companion-business.md](companion-business.md).