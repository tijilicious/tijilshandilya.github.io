import reflex as rx
from ..styles import (
    INK, INK2, INK3, PAPER, PAPER2, LINE,
    ACCENT, DTDL_PINK, TIRA_RED, MX_ORANGE, BYJUS_PURPLE,
    metric_val_style, metric_lbl_style, proj_text_style,
)
from ..state import State


# ── Shared sub-components ─────────────────────────────────────────────────────

def section_divider(label: str) -> rx.Component:
    return rx.flex(
        rx.box(class_name="exp-divider-line"),
        rx.text(label, font_size=".7rem", letter_spacing=".1em", color=INK3,
                text_transform="uppercase", font_weight="500", white_space="nowrap", padding="0 10px"),
        rx.box(class_name="exp-divider-line"),
        align_items="center", padding=".75rem 3rem", background=PAPER2,
        class_name="reveal",
    )


def metric(val: str, label: str, bg: str, val_color: str) -> rx.Component:
    return rx.box(
        rx.text(val,   **metric_val_style, color=val_color),
        rx.text(label, **metric_lbl_style),
        background=bg, padding=".85rem .5rem", text_align="center",
    )


def proj_row(title: str, desc: str, badge: str,
             row_bg: str, border_color: str, dot_color: str, badge_style: dict) -> rx.Component:
    return rx.flex(
        rx.box(width="6px", height="6px", border_radius="50%",
               background=dot_color, margin_top="5px", flex_shrink="0"),
        rx.text(
            rx.el.strong(title), f" — {desc}",
            **proj_text_style,
        ),
        rx.text(badge, **badge_style, font_size=".68rem", font_weight="600",
                padding=".15rem .6rem", white_space="nowrap", margin_left="auto", flex_shrink="0"),
        align_items="flex-start", gap=".6rem", padding=".65rem .85rem",
        background=row_bg, border_left=f"2px solid {border_color}",
    )


def tool_pill(label: str, style: dict) -> rx.Component:
    return rx.text(label, font_size=".7rem", font_weight="500", padding=".2rem .65rem", **style)


# ── DTDL ─────────────────────────────────────────────────────────────────────

def dtdl_card() -> rx.Component:
    return rx.box(
        # "CURRENT ROLE" badge (CSS-positioned)
        rx.text("CURRENT ROLE", class_name="dtdl-current-badge"),
        # Brand bar
        rx.flex(
            rx.flex(
                rx.box(
                    "T", width="32px", height="32px", background=DTDL_PINK,
                    display="flex", align_items="center", justify_content="center",
                    color="white", font_size="1.1rem", font_weight="900",
                    font_family="'Syne',sans-serif",
                ),
                rx.box(
                    rx.text("Deutsche Telekom", font_size=".85rem", font_weight="700", color=INK, line_height="1.2"),
                    rx.text("Digital Labs · India", font_size=".65rem", color="#888", font_weight="400", letter_spacing=".04em"),
                ),
                gap=".6rem", align_items="center",
            ),
            rx.text("Senior Data Analyst", background=DTDL_PINK, color="white",
                    font_size=".6rem", font_weight="700", letter_spacing=".08em",
                    padding=".3rem .9rem", text_transform="uppercase"),
            justify_content="space-between", align_items="center", margin_bottom="1.25rem",
        ),
        rx.text("Senior Data Analyst — OneTV Platform", font_size=".9rem", font_weight="600", margin_bottom=".25rem", color=INK),
        rx.flex(
            rx.text("📅 Jul 2025 – Present"), rx.text("📍 Gurugram, HR"), rx.text("📺 TV & OTT / Telecom"),
            gap="1rem", font_size=".75rem", color=INK3, margin_bottom="1.25rem", flex_wrap="wrap",
        ),
        # Metrics
        rx.grid(
            metric("OneTV", "Platform",     "#fff", DTDL_PINK),
            metric("EU",    "Market Scope", "#fff", DTDL_PINK),
            metric("🏆",    "ElevateX Winner", "#fff", DTDL_PINK),
            metric("Athena","AWS Stack",    "#fff", DTDL_PINK),
            grid_template_columns="repeat(4,1fr)", gap="1px",
            background="#fce8f3", border="1px solid #fce8f3", margin_bottom="1.25rem",
            class_name="metrics-grid",
        ),
        # Projects
        rx.flex(
            proj_row("OneTV Analytics",
                     "Senior Data Analyst for Deutsche Telekom's TV & OTT aggregation platform; built Metabase views to analyse watch duration and playback distribution across Live TV and VOD",
                     "Live TV · VOD", "#fff0f7", DTDL_PINK, DTDL_PINK,
                     dict(background="#fff0f7", color="#a00055")),
            proj_row("Inactive User Cohort Analysis",
                     "Ad-hoc analysis to identify inactive user cohorts using dynamic activity windows",
                     "Cohorts", "#fff0f7", DTDL_PINK, DTDL_PINK,
                     dict(background="#fff0f7", color="#a00055")),
            proj_row("ElevateX — Internal Competition Winner",
                     "Won DTDL's internal innovation competition as part of a team of 4, delivering a working solution to a real business problem",
                     "🏆 Winner", "#fff0f7", DTDL_PINK, DTDL_PINK,
                     dict(background="#fff0f7", color="#a00055")),
            direction="column", gap=".4rem", margin_bottom="1.25rem",
        ),
        # Tools
        rx.flex(
            *[tool_pill(t, dict(background="#fff0f7", color="#a00055", border=f"1px solid #f9c0de"))
              for t in ["AWS Athena","SQL","Metabase","Python","OTT Analytics"]],
            flex_wrap="wrap", gap=".35rem",
        ),
        padding="2rem 3rem", background="white", border_top=f"3px solid {DTDL_PINK}",
        position="relative", overflow="hidden", class_name="exp-card-pad reveal",
    )


# ── TIRA ─────────────────────────────────────────────────────────────────────

def tira_card() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text("TIRA", rx.el.sup("®", style={"font_size":".6rem","color":TIRA_RED,"vertical_align":"super"}),
                    font_family="'Cormorant Garamond',serif", font_size="1.6rem", font_weight="700",
                    letter_spacing=".12em", color=INK),
            rx.text("Deputy Manager — BI", background=TIRA_RED, color="white",
                    font_size=".6rem", font_weight="700", letter_spacing=".08em",
                    padding=".3rem .9rem", text_transform="uppercase"),
            justify_content="space-between", align_items="center", margin_bottom="1.25rem",
        ),
        rx.text("Business Intelligence & Strategy · Bengaluru", font_size=".9rem", font_weight="600", margin_bottom=".25rem", color=INK),
        rx.flex(
            rx.text("📅 Jul 2024 – Jul 2025"), rx.text("📍 Bengaluru, KA"), rx.text("🏪 Reliance Retail"),
            gap="1rem", font_size=".75rem", color=INK3, margin_bottom="1.25rem", flex_wrap="wrap",
        ),
        rx.grid(
            metric("BI",   "Data Owner",  "#fff", TIRA_RED),
            metric("100M+","User Base",   "#fff", TIRA_RED),
            metric("2",    "Key Projects","#fff", TIRA_RED),
            metric("S&P",  "Team",        "#fff", TIRA_RED),
            grid_template_columns="repeat(4,1fr)", gap="1px",
            background="#e5e5e5", border="1px solid #e5e5e5", margin_bottom="1.25rem",
            class_name="metrics-grid",
        ),
        rx.flex(
            proj_row("Seller Cancellation Analysis",
                     "Revenue impact, cart size analysis & reward optimisation to reduce churn at cancellation touchpoints",
                     "Revenue", "#fff7f6", TIRA_RED, TIRA_RED, dict(background="#fff0ee", color="#c01400")),
            proj_row("Sample Activation Metrics",
                     "Built reporting structure and success metrics for on-site sampling activations",
                     "Reporting", "#fff7f6", TIRA_RED, TIRA_RED, dict(background="#fff0ee", color="#c01400")),
            direction="column", gap=".4rem", margin_bottom="1.25rem",
        ),
        rx.flex(
            *[tool_pill(t, dict(background="#fff0ee", color="#c01400", border="1px solid #ffd4ce"))
              for t in ["SQL","Python","Tableau","Data Studio","Revenue Analytics"]],
            flex_wrap="wrap", gap=".35rem",
        ),
        padding="2rem 3rem", background="white", border_top=f"3px solid {TIRA_RED}",
        class_name="exp-card-pad reveal",
    )


# ── MX PLAYER ────────────────────────────────────────────────────────────────

def mx_card() -> rx.Component:
    MX_DARK = "#0f0f0f"
    return rx.box(
        rx.flex(
            rx.flex(
                rx.box("MX", background=MX_ORANGE, color="white", font_size=".85rem",
                       font_weight="800", padding=".25rem .5rem"),
                rx.text("Player", color="white", font_size=".9rem", font_weight="600", letter_spacing=".04em"),
                gap=".4rem", align_items="center",
            ),
            rx.text("Growth Insight Analyst", background="#1e1e1e", color=MX_ORANGE,
                    font_size=".6rem", font_weight="700", letter_spacing=".08em",
                    padding=".3rem .9rem", text_transform="uppercase", border="1px solid #2a2a2a"),
            justify_content="space-between", align_items="center", margin_bottom="1.25rem",
        ),
        rx.text("Associate — Growth Insight Analyst", font_size=".9rem", font_weight="600", margin_bottom=".25rem", color="white"),
        rx.flex(
            rx.text("📅 Jul 2022 – Jul 2024"), rx.text("📍 Mumbai, MH"), rx.text("🎬 OTT / Streaming"),
            gap="1rem", font_size=".75rem", color="#666", margin_bottom="1.25rem", flex_wrap="wrap",
        ),
        rx.grid(
            metric("+21%", "CTR Lift",      "#111", MX_ORANGE),
            metric("5×",   "Local Revenue", "#111", MX_ORANGE),
            metric("+85%", "OTT Watch Time","#111", MX_ORANGE),
            metric("+12%", "iOS Engagement","#111", MX_ORANGE),
            grid_template_columns="repeat(4,1fr)", gap="1px",
            background="#1e1e1e", border="1px solid #1e1e1e", margin_bottom="1.25rem",
            class_name="metrics-grid",
        ),
        rx.flex(
            proj_row("Search Optimisation",
                     "Improved overall watch time by 7%, trending CTR by 21%, trending watch share from 3% to 11%",
                     "+7% WT", "#161616", MX_ORANGE, MX_ORANGE,
                     dict(background="#1e1e1e", color=MX_ORANGE, border="1px solid #2a2a2a")),
            proj_row("Local Pack",
                     "5× revenue from local subscribed users; +85% OTT watch time from regional content",
                     "5× Rev", "#161616", MX_ORANGE, MX_ORANGE,
                     dict(background="#1e1e1e", color=MX_ORANGE, border="1px solid #2a2a2a")),
            proj_row("iOS Continue Watching",
                     "Persistent bottom bar boosted watch history stickiness by 12%",
                     "+12%", "#161616", MX_ORANGE, MX_ORANGE,
                     dict(background="#1e1e1e", color=MX_ORANGE, border="1px solid #2a2a2a")),
            proj_row("Ads Reporting Automation",
                     "Fully automated daily ad metrics pipeline via Python, Google App Script & Ads Manager",
                     "Auto", "#161616", MX_ORANGE, MX_ORANGE,
                     dict(background="#1e1e1e", color=MX_ORANGE, border="1px solid #2a2a2a")),
            direction="column", gap=".4rem", margin_bottom="1.25rem",
        ),
        rx.flex(
            *[tool_pill(t, dict(background="#1a1a1a", color="#777", border="1px solid #222"))
              for t in ["BigQuery","Python","SQL","Google App Script","Ads Manager","Data Studio"]],
            flex_wrap="wrap", gap=".35rem",
        ),
        padding="2rem 3rem", background=MX_DARK, border_top=f"3px solid {MX_ORANGE}",
        class_name="exp-card-pad reveal",
    )


# ── BYJU'S ───────────────────────────────────────────────────────────────────

def byjus_card() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.box("🎓", width="28px", height="28px", background=BYJUS_PURPLE,
                       border_radius="6px", display="flex", align_items="center",
                       justify_content="center", font_size=".75rem"),
                rx.flex(
                    rx.text("BYJU'S ", font_family="'Nunito',sans-serif", font_size="1rem",
                            font_weight="900", color=BYJUS_PURPLE, display="inline"),
                    rx.text("Exam Prep", font_family="'Nunito',sans-serif", font_size="1rem",
                            font_weight="900", color="#F59E0B", display="inline"),
                ),
                gap=".5rem", align_items="center",
            ),
            rx.text("Data Analyst", background="#EEE8FF", color=BYJUS_PURPLE,
                    font_size=".6rem", font_weight="700", letter_spacing=".08em",
                    padding=".3rem .9rem", border_radius="20px", text_transform="uppercase"),
            justify_content="space-between", align_items="center", margin_bottom="1rem",
        ),
        # "First role" live pill
        rx.flex(
            rx.box(class_name="live-dot"),
            rx.text(" First role — foundation built here",
                    font_size=".7rem", font_weight="700", color="#cc2200"),
            align_items="center", gap=".35rem",
            background="#FFF4F4", border="1px solid #FFD0D0", padding=".25rem .7rem",
            border_radius="20px", margin_bottom=".9rem", display="inline-flex",
        ),
        rx.text("Data Analyst · Noida, UP", font_size=".9rem", font_weight="600", margin_bottom=".25rem", color=INK),
        rx.flex(
            rx.text("📅 Jun 2021 – Jun 2022"), rx.text("📍 Noida, UP"), rx.text("💻 EdTech"),
            gap="1rem", font_size=".75rem", color=INK3, margin_bottom="1.25rem", flex_wrap="wrap",
        ),
        rx.grid(
            metric("3",    "Teams Served",   "#f8f7fe", BYJUS_PURPLE),
            metric("4+",   "Tools Used",     "#f8f7fe", BYJUS_PURPLE),
            metric("DQ",   "Quality Lead",   "#f8f7fe", BYJUS_PURPLE),
            metric("3Cr+", "Platform Users", "#f8f7fe", BYJUS_PURPLE),
            grid_template_columns="repeat(4,1fr)", gap="1px",
            background="#e5e5e5", border="1px solid #e5e5e5", margin_bottom="1.25rem",
            class_name="metrics-grid",
        ),
        rx.flex(
            proj_row("Cross-functional Analytics",
                     "Data solutions for Customer Experience, Growth & Marketing, and Revenue teams",
                     "3 Teams", "#f8f7fe", BYJUS_PURPLE, BYJUS_PURPLE,
                     dict(background="#EEE8FF", color="#4a22c0", border_radius="20px")),
            proj_row("BI Visualisation",
                     "Built dashboards and reports using BigQuery, Python, Tableau & Data Studio",
                     "Viz", "#f8f7fe", BYJUS_PURPLE, BYJUS_PURPLE,
                     dict(background="#EEE8FF", color="#4a22c0", border_radius="20px")),
            proj_row("Data Quality Ownership",
                     "Supervised data integrity and workflow quality across all team pipelines",
                     "DQ", "#f8f7fe", BYJUS_PURPLE, BYJUS_PURPLE,
                     dict(background="#EEE8FF", color="#4a22c0", border_radius="20px")),
            direction="column", gap=".4rem", margin_bottom="1.25rem",
        ),
        rx.flex(
            *[tool_pill(t, dict(background="#f3f0ff", color="#5030b0", border="1px solid #ddd8f8", border_radius="20px"))
              for t in ["SQL / BigQuery","Python","Tableau","Data Studio","Pandas"]],
            flex_wrap="wrap", gap=".35rem",
        ),
        padding="2rem 3rem", background="white", border_top=f"3px solid {BYJUS_PURPLE}",
        class_name="exp-card-pad reveal",
    )


# ── Section ───────────────────────────────────────────────────────────────────

def experience() -> rx.Component:
    return rx.box(
        # Header
        rx.flex(
            rx.text("01", font_family="'Syne',sans-serif", font_size=".75rem",
                    color=ACCENT, letter_spacing=".1em"),
            rx.heading("Experience", font_family="'Syne',sans-serif", font_size="2rem",
                       font_weight="700", letter_spacing="-.02em", color=INK, as_="h2"),
            rx.box(flex="1", height="1px", background=LINE),
            align_items="baseline", gap="1.5rem", margin_bottom="3rem",
            padding="0 3rem", class_name="reveal",
        ),
        section_divider("Deutsche Telekom Digital Labs · Gurugram"),
        dtdl_card(),
        section_divider("Tira · Reliance Retail"),
        tira_card(),
        section_divider("MX Player · Mumbai"),
        mx_card(),
        section_divider("BYJU'S Exam Prep · Noida"),
        byjus_card(),
        id="experience",
        background=PAPER2,
        border_top=f"1px solid {LINE}",
        padding="5rem 0",
    )
