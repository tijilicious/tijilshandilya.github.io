import reflex as rx
from ..styles import INK, INK2, INK3, PAPER3, ACCENT, LINE
from ..state import State

ANALYTICS_SKILLS = [
    ("SQL",          95),
    ("Python",       85),
    ("BigQuery",     88),
    ("Pandas",       82),
    ("scikit-learn", 65),
]

VIZ_SKILLS = [
    ("Tableau",      88),
    ("Data Studio",  90),
    ("Google Ads",   78),
    ("App Script",   75),
    ("NumPy",        80),
]


def skill_bar(name: str, pct: int, animated: bool) -> rx.Component:
    return rx.flex(
        rx.text(name, font_size=".85rem", width="100px", flex_shrink="0", color=INK),
        rx.box(
            rx.box(
                class_name=f"skill-fill {'animated' if animated else ''}",
                style={"--target-width": f"{pct}%"},
            ),
            flex="1", height="3px", background=PAPER3,
        ),
        rx.text(f"{pct}%", font_size=".75rem", color=INK3, width="32px", text_align="right"),
        align_items="center", gap="1rem",
    )


def skill_group(title: str, skills: list, animated: bool) -> rx.Component:
    return rx.box(
        rx.text(title, font_size=".7rem", text_transform="uppercase",
                letter_spacing=".1em", color=INK3, margin_bottom="1rem"),
        rx.flex(
            *[skill_bar(name, pct, animated) for name, pct in skills],
            direction="column", gap=".85rem",
        ),
    )


def skills() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text("02", font_family="'Syne',sans-serif", font_size=".75rem",
                    color=ACCENT, letter_spacing=".1em"),
            rx.heading("Skills", font_family="'Syne',sans-serif", font_size="2rem",
                       font_weight="700", letter_spacing="-.02em", color=INK, as_="h2"),
            rx.box(flex="1", height="1px", background=LINE),
            align_items="baseline", gap="1.5rem", margin_bottom="3rem",
            class_name="reveal",
        ),
        rx.grid(
            skill_group("Data & Analytics",   ANALYTICS_SKILLS, State.skills_visible),
            skill_group("Visualisation & BI", VIZ_SKILLS,       State.skills_visible),
            grid_template_columns="1fr 1fr", gap="4rem", class_name="skills-grid",
            # Trigger skill animation and analytics when this grid enters viewport
            id="skills-grid",
        ),
        id="skills",
        padding="5rem 3rem",
        border_top=f"1px solid {LINE}",
    )
