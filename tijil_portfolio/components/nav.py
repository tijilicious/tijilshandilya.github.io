import reflex as rx
from ..styles import INK, INK2, PAPER, ACCENT, LINE
from ..state import State


def nav() -> rx.Component:
    return rx.box(
        # Logo
        rx.text(
            "T", rx.el.span(".", class_name="nav-logo-span"), "S",
            font_family="'Syne', sans-serif", font_weight="800",
            font_size="1.1rem", letter_spacing="-.02em", color=INK,
        ),
        # Links
        rx.flex(
            rx.link("Experience", href="#experience", class_name="nav-link hide-mobile"),
            rx.link("Skills",     href="#skills",     class_name="nav-link hide-mobile"),
            rx.link("Ask AI",     href="#ai-section", class_name="nav-link hide-mobile"),
            gap="2rem", align_items="center",
        ),
        # CTA
        rx.el.a(
            "Get in Touch",
            href="mailto:shan.tijilicious@gmail.com",
            class_name="nav-contact-btn",
            on_click=State.track_cta_click("nav_contact", "mailto:shan.tijilicious@gmail.com"),
        ),
        position="fixed", top="0", left="0", right="0", z_index="200",
        display="flex", align_items="center", justify_content="space-between",
        padding="1rem 3rem",
        background="rgba(250,248,244,0.92)",
        backdrop_filter="blur(14px)",
        border_bottom=f"1px solid {LINE}",
    )
