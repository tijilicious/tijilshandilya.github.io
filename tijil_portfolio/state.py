"""
Centralised application state.
All API calls (Anthropic + GA4 analytics) happen here — server-side.
"""
import os
import uuid
import httpx
import reflex as rx
from dotenv import load_dotenv

from .analytics import (
    track_page_view, track_cta, track_chat_sent,
    track_chat_response, track_experience_viewed,
    track_skills_viewed, track_scroll_depth,
)

load_dotenv()

# ── Resume context for the AI assistant ──────────────────────────────────────
RESUME_CONTEXT = """You are the portfolio assistant for Tijil Shandilya, a Senior Data Analyst with 4+ years of experience. Answer questions about him in a professional, helpful tone. Keep answers concise (2–4 sentences). Highlight numbers and outcomes wherever possible.

FULL BACKGROUND:
Name: Tijil Shandilya | Email: shan.tijilicious@gmail.com | Phone: 7906901931 | LinkedIn: linkedin.com/in/tijil-shandilya

EDUCATION: B.Tech Electrical & Electronics Engineering, JSS ATEN Noida, 2017–2021, CGPA 7.47.

WORK EXPERIENCE:

1. Deutsche Telekom Digital Labs (DTDL) — Senior Data Analyst, OneTV Platform | Jul 2025–Present | Gurugram
   OneTV is Deutsche Telekom's TV & OTT aggregation platform serving European markets.
   - Built Metabase views to analyse watch duration and playback distribution across Live TV and VOD.
   - Performed ad-hoc analysis to identify inactive user cohorts using dynamic activity windows.
   - Working with AWS Athena (SQL) and Metabase for analytics and reporting.
   - Won ElevateX internal competition (team of 4) delivering a working solution to a real business problem.

2. Tira (Reliance Retail) — Deputy Manager, Business Intelligence | Jul 2024–Jul 2025 | Bengaluru
   - Owned BI requirements for Strategy & Projects team.
   - Analysed seller cancellations and revenue impact.
   - Designed success metrics for on-site sampling.

3. MX Player — Associate Growth Insight Analyst | Jul 2022–Jul 2024 | Mumbai
   - Search Optimisation: +7% watch time, +21% trending CTR, watch time share 3%→11%.
   - Local Pack: 5× revenue from local subscribed users, +85% OTT watch time.
   - Android Product: video CTR +7%, engagement +3%.
   - Ad Load Time: −0.4ms ad initialisation via ad caching.
   - iOS Continue Watching: +12% watch history engagement.
   - Ads Automation: Python + Google App Script + Ads Manager pipeline.

4. BYJU'S ExamPrep — Data Analyst | Jun 2021–Jun 2022 | Noida
   - Built dashboards using BigQuery, Python, Tableau & Data Studio.
   - Delivered analytics for CX, growth, marketing & revenue teams.
   - Ensured data quality across reporting workflows.

SKILLS: SQL, Python, AWS Athena, Metabase, Tableau, Data Studio, Pandas, NumPy, scikit-learn, BigQuery, Google Ads Manager, Google App Script.
CERTIFICATIONS: Programming for Everybody (U of Michigan), Python Data Structures (U of Michigan), SEO (UC Davis), Marketing in a Digital World (UIUC).
LANGUAGES: English, Hindi.
LEADERSHIP: Business Head – Team Vega Racing (ESI & SAE BAJA). Core Member – SPADE."""


# ── Data model ───────────────────────────────────────────────────────────────
class Message(rx.Base):
    role: str   # "user" | "ai"
    text: str


# ── Application State ────────────────────────────────────────────────────────
class State(rx.State):
    # Session-scoped anonymous ID used for GA4 Measurement Protocol
    client_id: str = ""

    # Chat
    messages: list[Message] = [
        Message(role="ai", text="Hi! I'm Tijil's portfolio assistant. Ask me about his experience, projects, skills, or anything else you'd like to know.")
    ]
    chat_input: str = ""
    chat_loading: bool = False

    # Skills animation trigger
    skills_visible: bool = False

    # Scroll depth milestones already fired (serialised as comma-separated string)
    _depth_fired: str = ""

    # ── Lifecycle ──────────────────────────────────────────────────────────────
    def on_load(self):
        """Called when the page first loads."""
        if not self.client_id:
            self.client_id = str(uuid.uuid4())

    async def on_page_ready(self):
        """Fire page_view once client_id is set."""
        await track_page_view(self.client_id)

    # ── CTA tracking ──────────────────────────────────────────────────────────
    async def track_cta_click(self, label: str, destination: str):
        await track_cta(self.client_id, label, destination)

    # ── Experience card tracking ───────────────────────────────────────────────
    async def track_exp_viewed(self, company: str):
        await track_experience_viewed(self.client_id, company)

    # ── Skills section ────────────────────────────────────────────────────────
    async def trigger_skills(self):
        """Called from JS IntersectionObserver when skills enter viewport."""
        if not self.skills_visible:
            self.skills_visible = True
            await track_skills_viewed(self.client_id)

    # ── Scroll depth ──────────────────────────────────────────────────────────
    async def on_scroll_milestone(self, depth: int):
        key = str(depth)
        if key not in self._depth_fired.split(","):
            self._depth_fired += f",{key}"
            await track_scroll_depth(self.client_id, depth)

    # ── Chat ──────────────────────────────────────────────────────────────────
    def set_chat_input(self, value: str):
        self.chat_input = value

    async def send_message(self, text: str = ""):
        query = (text or self.chat_input).strip()
        if not query or self.chat_loading:
            return

        self.chat_input = ""
        self.messages = [*self.messages, Message(role="user", text=query)]
        self.chat_loading = True
        yield  # Push user message + spinner to browser immediately

        is_suggestion = bool(text)  # suggestion bypasses the input field
        await track_chat_sent(self.client_id, len(query), is_suggestion)

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    "https://api.anthropic.com/v1/messages",
                    headers={
                        "x-api-key": os.getenv("ANTHROPIC_API_KEY", ""),
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json",
                    },
                    json={
                        "model": "claude-3-5-haiku-20241022",
                        "max_tokens": 1000,
                        "system": RESUME_CONTEXT,
                        "messages": [{"role": "user", "content": query}],
                    },
                    timeout=30.0,
                )
                data = resp.json()
                reply = "".join(b.get("text", "") for b in data.get("content", []))
                reply = reply or "No response received."
                await track_chat_response(self.client_id, True, len(reply))
        except Exception:
            reply = "Something went wrong — please try again."
            await track_chat_response(self.client_id, False)

        self.messages = [*self.messages, Message(role="ai", text=reply)]
        self.chat_loading = False

    async def send_suggestion(self, suggestion: str):
        await self.send_message(suggestion)
