"""
Tijil Shandilya — Portfolio
Full-stack Python with Reflex.
  • UI:        Pure Python (Reflex components)
  • AI Chat:   Anthropic API called server-side (key never exposed to browser)
  • Analytics: GA4 Measurement Protocol via httpx (no JS SDK)
  • JS:        Only a tiny scroll/skills observer — unavoidable for UX animations
"""
import reflex as rx
from .components import nav, hero, experience, skills, ai_chat, footer
from .state import State

# ── Minimal JavaScript for scroll-reveal + skill bar animation ────────────────
# This is the only JavaScript in the entire project.
_OBSERVER_JS = """
(function () {
  // Scroll-reveal
  const revObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach(el => revObs.observe(el));

  // Skills bar animation — calls Python state via Reflex event
  const skillsGrid = document.getElementById('skills-grid');
  if (skillsGrid) {
    const skillObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          // Animate CSS bars
          e.target.querySelectorAll('.skill-fill').forEach(b => b.classList.add('animated'));
          // Notify Python state (tracks analytics + updates skills_visible)
          window.__reflex?.event('trigger_skills');
          skillObs.unobserve(e.target);
        }
      });
    }, { threshold: 0.3 });
    skillObs.observe(skillsGrid);
  }

  // Scroll-depth milestones — notifies Python state
  const milestones = new Set();
  window.addEventListener('scroll', () => {
    const pct = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);
    [25, 50, 75, 100].forEach(m => {
      if (pct >= m && !milestones.has(m)) {
        milestones.add(m);
        window.__reflex?.event('on_scroll_milestone', m);
      }
    });
  }, { passive: true });

  // Auto-scroll chat to bottom on new messages
  const chatMsgs = document.getElementById('chat-messages');
  if (chatMsgs) {
    new MutationObserver(() => { chatMsgs.scrollTop = chatMsgs.scrollHeight; })
      .observe(chatMsgs, { childList: true, subtree: true });
  }
})();
"""


def index() -> rx.Component:
    return rx.box(
        # Google Fonts + global CSS
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800"
                 "&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300"
                 "&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400"
                 "&family=Nunito:wght@700;800;900&display=swap",
        ),
        # Page sections
        nav(),
        hero(),
        experience(),
        skills(),
        ai_chat(),
        footer(),
        # Scroll + animation observer (the only JS in this project)
        rx.script(_OBSERVER_JS),
        # Fire page_view analytics on load
        on_mount=State.on_page_ready,
    )


app = rx.App(
    stylesheets=["global.css"],   # served from assets/global.css
    head_components=[
        rx.el.meta(name="description",
                   content="Senior Data Analyst at Deutsche Telekom Digital Labs with 5+ years of experience in BI, growth analytics and data visualisation."),
        rx.el.title("Tijil Shandilya — Senior Data Analyst"),
    ],
)
app.add_page(index, route="/", on_load=State.on_load)
