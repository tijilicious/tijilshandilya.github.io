# Setup Guide — Python Portfolio (Reflex)

## What is Reflex?
Reflex (reflex.dev) is a **100% Python** full-stack web framework.
You write Python — it handles the server, the UI, and state management.
No HTML, no CSS files you have to edit, no JavaScript to write.

---

## 1 · Install Python 3.11+
Download from https://python.org. Confirm with:
```bash
python --version
```

## 2 · Create a virtual environment & install dependencies
```bash
cd tijil-portfolio-python
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## 3 · Add your secrets
```bash
cp .env.example .env
```
Then open `.env` and fill in:

### Anthropic API Key (AI Chat)
Get from https://console.anthropic.com → API Keys
```
ANTHROPIC_API_KEY=sk-ant-...
```
The key is used **server-side only** — it is never sent to the browser.

### GA4 Analytics (optional but recommended)
1. Go to https://console.firebase.google.com → your project → Google Analytics
2. GA4 Admin → Data Streams → select your web stream
3. Copy the **Measurement ID** (G-XXXXXXXXXX)
4. Click **Measurement Protocol API secrets** → Create a secret
```
GA_MEASUREMENT_ID=G-XXXXXXXXXX
GA_API_SECRET=your_secret_here
```
All events are fired **server-side** via the GA4 Measurement Protocol — no Firebase JS SDK needed.

## 4 · Run locally
```bash
reflex run
```
Opens at **http://localhost:3000**  
Backend runs at http://localhost:8000

## 5 · Build for production
```bash
reflex export --frontend-only   # static export (if no backend needed)
# or deploy to Reflex Cloud:
reflex deploy
```

---

## Project structure
```
tijil-portfolio-python/
├── rxconfig.py                   ← Reflex config
├── requirements.txt
├── .env                          ← your secrets (never commit this)
├── assets/
│   └── global.css                ← CSS tokens, animations, responsive rules
└── tijil_portfolio/
    ├── tijil_portfolio.py        ← app entry point + page definition
    ├── state.py                  ← ALL application state + API calls
    ├── analytics.py              ← GA4 Measurement Protocol helpers
    ├── styles.py                 ← design token constants
    └── components/
        ├── nav.py
        ├── hero.py
        ├── experience.py
        ├── skills.py
        ├── ai_chat.py
        └── footer.py
```

## Analytics events tracked (all server-side, pure Python)
| Event | When |
|---|---|
| `page_view` | App load |
| `cta_click` | Nav / hero / footer buttons |
| `chat_message_sent` | Every AI chat message |
| `chat_response_received` | After AI reply (success + length) |
| `experience_card_viewed` | Each company card enters viewport |
| `skills_section_viewed` | Skill bars enter viewport |
| `scroll_depth` | 25 / 50 / 75 / 100% scroll milestones |
