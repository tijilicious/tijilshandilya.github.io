# ── Design Tokens ────────────────────────────────────────────────────────────
INK    = "#0f0e0d"
INK2   = "#3a3835"
INK3   = "#7a7570"
PAPER  = "#faf8f4"
PAPER2 = "#f2efe8"
PAPER3 = "#e8e4da"
ACCENT = "#c94a2a"
LINE   = "rgba(15,14,13,0.1)"

# ── Common reusable style dicts ───────────────────────────────────────────────
section_header = dict(
    display="flex", align_items="baseline", gap="1.5rem", margin_bottom="3rem",
)
section_num_style = dict(
    font_family="'Syne', sans-serif", font_size=".75rem", color=ACCENT, letter_spacing=".1em",
)
section_title_style = dict(
    font_family="'Syne', sans-serif", font_size="2rem", font_weight="700", letter_spacing="-.02em",
    color=INK,
)
section_line_style = dict(flex="1", height="1px", background=LINE)

metric_val_style = dict(font_size="1.25rem", font_weight="700", line_height="1", margin_bottom=".15rem")
metric_lbl_style = dict(font_size=".65rem", text_transform="uppercase", letter_spacing=".06em", opacity=".6")
proj_text_style  = dict(font_size=".82rem", line_height="1.55", flex="1", color=INK2)
tool_pill_base   = dict(font_size=".7rem", font_weight="500", padding=".2rem .65rem")

role_line_style = dict(font_size=".9rem", font_weight="600", margin_bottom=".25rem", color=INK)
period_loc_style = dict(font_size=".75rem", color=INK3, margin_bottom="1.25rem")

# ── Brand colours ─────────────────────────────────────────────────────────────
DTDL_PINK  = "#E10075"
TIRA_RED   = "#F11A00"
MX_ORANGE  = "#FF6C00"
BYJUS_PURPLE = "#6C3CE1"
