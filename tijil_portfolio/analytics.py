"""
Pure-Python Firebase / GA4 analytics via the Measurement Protocol.
All events fire server-side — no JavaScript SDK required.

Setup:
  GA_MEASUREMENT_ID → GA4 Admin → Data Streams → your stream → Measurement ID
  GA_API_SECRET     → same page → Measurement Protocol API secrets → Create
"""
import os
import httpx

_MP_URL = "https://www.google-analytics.com/mp/collect"


async def _fire(client_id: str, event_name: str, params: dict) -> None:
    measurement_id = os.getenv("GA_MEASUREMENT_ID", "")
    api_secret     = os.getenv("GA_API_SECRET", "")
    if not measurement_id or not api_secret:
        return  # silently skip if not configured

    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                _MP_URL,
                params={"measurement_id": measurement_id, "api_secret": api_secret},
                json={
                    "client_id": client_id or "anonymous",
                    "events": [{"name": event_name, "params": params}],
                },
                timeout=5.0,
            )
    except Exception:
        pass  # analytics must never break the UI


# ── Typed helpers (called from State event handlers) ──────────────────────────

async def track_page_view(client_id: str) -> None:
    await _fire(client_id, "page_view", {"page_title": "Tijil Shandilya — Portfolio"})

async def track_cta(client_id: str, label: str, destination: str) -> None:
    await _fire(client_id, "cta_click", {"label": label, "destination": destination})

async def track_chat_sent(client_id: str, query_len: int, is_suggestion: bool) -> None:
    await _fire(client_id, "chat_message_sent", {
        "query_length": query_len,
        "is_quick_suggestion": is_suggestion,
    })

async def track_chat_response(client_id: str, success: bool, response_len: int = 0) -> None:
    await _fire(client_id, "chat_response_received", {
        "success": success,
        "response_length": response_len,
    })

async def track_experience_viewed(client_id: str, company: str) -> None:
    await _fire(client_id, "experience_card_viewed", {"company": company})

async def track_skills_viewed(client_id: str) -> None:
    await _fire(client_id, "skills_section_viewed", {})

async def track_scroll_depth(client_id: str, depth_pct: int) -> None:
    await _fire(client_id, "scroll_depth", {"depth_percent": depth_pct})
