import reflex as rx
from ..styles import INK, PAPER2, PAPER3, ACCENT, LINE
from ..state import State


def footer() -> rx.Component:
    return rx.el.footer(
        rx.box(
            rx.text("Tijil Shandilya",
                    font_family="'Syne',sans-serif", font_weight="800", font_size="1.1rem"),
            rx.text("Senior Data Analyst · Gurugram, India",
                    font_size=".75rem", color="#7a7570", margin_top=".2rem"),
        ),
        rx.flex(
            rx.el.a(
                "shan.tijilicious@gmail.com",
                href="mailto:shan.tijilicious@gmail.com",
                font_size=".8rem", color=PAPER3,
                on_click=State.track_cta_click("footer_email", "mailto:shan.tijilicious@gmail.com"),
                style={"transition": "color .2s", "_hover": {"color": ACCENT}},
            ),
            rx.el.a(
                "GitHub ↗",
                href="https://github.com/tijilshandilya",
                target="_blank",
                font_size=".8rem", color=PAPER3,
                on_click=State.track_cta_click("footer_github", "https://github.com/tijilshandilya"),
                style={"transition": "color .2s", "_hover": {"color": ACCENT}},
            ),
            rx.el.a(
                "LinkedIn ↗",
                href="https://www.linkedin.com/in/tijil-shandilya/",
                target="_blank",
                font_size=".8rem", color=PAPER3,
                on_click=State.track_cta_click("footer_linkedin", "https://www.linkedin.com/in/tijil-shandilya/"),
                style={"transition": "color .2s", "_hover": {"color": ACCENT}},
            ),
            gap="1.5rem", class_name="f-links",
        ),
        background=INK, color=PAPER2,
        padding="3rem",
        display="flex", justify_content="space-between", align_items="center",
        flex_wrap="wrap", gap="1.5rem",
        border_top=f"1px solid {LINE}",
        class_name="footer-flex",
    )
