# Building an AI Companion Business (the "next Candy AI" playbook)

Candy AI proved the market: people pay for AI girlfriends and boyfriends that
chat, send pictures, and talk. This guide maps that exact product — chat +
voice + images + memory — onto an open-source stack you own.

## The product map

| Candy AI feature | Your open-source equivalent |
|---|---|
| Chat | X/Friend turn engine (uncensored LLM) |
| Voice messages | SecretVoice TTS (`send_audio`) |
| Pics / edits | Wavespeed Qwen img2img from a fixed reference image (`send_image`) |
| Character creator | `xfriend init` → persona + config per companion |
| Memory | rolling "SCENE SO FAR" summary + durable facts |
| Web / mobile surface | API + any frontend, or start with the Telegram bot |

## The unit economics mindset

The stack is built for cheap, high-volume conversations:

- **Byte-stable personas** → prompt-caching → lower cost per turn.
- **Compaction** → old context rolls into a small summary instead of
  re-sending history → bounded tokens per session.
- **Flash-class LLM** + **per-character voice** pricing keep the marginal cost
  of a chat near-zero until you scale.
- **Per-chat isolation** (`build_companion(config, companion_id=...)`) → one
  deployment, thousands of paying users, each with their own memory.

Measure your own cost per session and price a subscription above it — the
point is you *can* hit profitable per-user numbers from day one.

## Monetization models that work

- **Freemium chat + paid voice/pictures** — text is cheap; make voice notes
  and image generation the premium tier.
- **Credit packs** — characters/tokens bundles (the same credit mechanic
  SecretVoice uses internally).
- **Subscription tiers** — unlimited chat, monthly voice minutes, X pictures.
- **Character marketplace** — let users create and sell persona packs.

## Memory at scale

Every user is an isolated companion:

```python
from xfriend.orchestrator import build_companion
companion = build_companion(config, companion_id=f"user-{user_id}")
```

JSON-file storage works to tens of thousands of chats; swap the
`MemoryStore` for Postgres/SQLite when you outgrow it — the protocol is three
methods.

## Compliance (the part everyone skips)

1. **Age-gating** — 18+ verification at signup; this content is adult.
2. **Payment processor policies** — Stripe/PayPal adult-content rules; many
   companion apps use third-party adult processors.
3. **Platform policies** — app stores and ad networks restrict NSFW AI;
   Telegram/self-hosting are the friendly surfaces.
4. **Model behavior** — keep an audit trail of what your companion says
   (the framework logs history + media to its store).
5. **Your jurisdiction** — the rules differ by country; get actual advice.

## The 10-minute MVP

1. `pip install xfriend xfriend-telegram`
2. `xfriend init mia` → write `persona.md`
3. Set keys (Venice + SecretVoice)
4. Run the Telegram bot — that's a live, paying-feature-shaped MVP
5. Add image gen (`base_image` + LoRAs), then the web API + billing

From there: measure cost per user, pick your pricing model, and ship.