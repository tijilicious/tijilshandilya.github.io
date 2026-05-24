import reflex as rx
from ..styles import INK, INK2, INK3, PAPER, PAPER2, PAPER3, ACCENT, LINE
from ..state import State

QUICK_SKILLS = ["SQL", "Python", "Tableau", "AWS Athena", "Metabase", "Pandas", "scikit-learn", "Data Studio"]

STATS = [
    ("5+",  "Years Experience"),
    ("4",   "Companies"),
    ("21%", "Max CTR Lift"),
    ("5×",  "Revenue Growth"),
]


def stat_cell(num: str, label: str) -> rx.Component:
    return rx.box(
        rx.text(num,   font_family="'Syne',sans-serif", font_weight="800", font_size="2.2rem", color=ACCENT, line_height="1"),
        rx.text(label, font_size=".75rem", color=INK3, text_transform="uppercase", letter_spacing=".08em", margin_top=".3rem"),
        background=PAPER2, padding="1.5rem",
    )


def hero() -> rx.Component:
    return rx.box(
        # ── Left ──────────────────────────────────────────────────────────────
        rx.flex(
            rx.text(
                "Senior Data Analyst — OneTV · Deutsche Telekom Digital Labs",
                class_name="hero-tag",
                font_size=".75rem", letter_spacing=".1em", text_transform="uppercase",
                color=ACCENT, margin_bottom="1.5rem",
            ),
            rx.heading(
                "Tijil", rx.el.br(),
                rx.el.em("Shandilya", style={"font_style": "normal", "color": ACCENT}),
                font_family="'Syne',sans-serif", font_weight="800",
                font_size="clamp(2.4rem,5vw,4.5rem)", line_height=".95",
                letter_spacing="-.03em", margin_bottom="1.5rem", color=INK,
                as_="h1",
            ),
            rx.text(
                "4+ years turning raw data into growth. Currently analysing TV & OTT behaviour at "
                "Deutsche Telekom's OneTV platform. Previously at Tira (Reliance Retail), MX Player & BYJU'S.",
                font_size="1rem", color=INK2, line_height="1.7", max_width="420px", margin_bottom="2.5rem",
            ),
            rx.flex(
                rx.el.a(
                    "Get in Touch", href="mailto:shan.tijilicious@gmail.com",
                    class_name="btn-primary",
                    on_click=State.track_cta_click("hero_contact", "mailto:shan.tijilicious@gmail.com"),
                ),
                rx.el.a(
                    "LinkedIn ↗",
                    href="https://www.linkedin.com/in/tijil-shandilya/",
                    target="_blank", class_name="btn-outline",
                    on_click=State.track_cta_click("hero_linkedin", "https://www.linkedin.com/in/tijil-shandilya/"),
                ),
                gap="1rem",
            ),
            direction="column", justify_content="center",
            padding="4rem 3rem", border_right=f"1px solid {LINE}",
        ),
        # ── Right ─────────────────────────────────────────────────────────────
        rx.flex(
            # Stats grid
            rx.grid(
                *[stat_cell(n, l) for n, l in STATS],
                grid_template_columns="1fr 1fr", gap="1px",
                background=LINE, border=f"1px solid {LINE}", margin_bottom="2rem",
            ),
            # Quick skills
            rx.flex(
                *[
                    rx.box(
                        skill,
                        font_size=".75rem", padding=".3rem .75rem",
                        border=f"1px solid {PAPER3}", background=PAPER, color=INK2, letter_spacing=".03em",
                    )
                    for skill in QUICK_SKILLS
                ],
                flex_wrap="wrap", gap=".5rem",
            ),
            direction="column", justify_content="center", padding="4rem 3rem", background=PAPER2,
        ),
        id="hero",
        min_height="100vh",
        display="grid",
        grid_template_columns="1fr 1fr",
        class_name="hero-grid",
        padding_top="4.5rem",
    )
