import reflex as rx
from ..styles import INK, INK2, INK3, PAPER, PAPER2, PAPER3, LINE
from ..state import State, Message

SUGGESTIONS = [
    "What's your biggest impact?",
    "Tell me about MX Player work",
    "What tools do you use?",
    "Why hire Tijil?",
]


def chat_bubble(message: Message) -> rx.Component:
    return rx.cond(
        message.role == "user",
        rx.box(
            message.text,
            align_self="flex-end",
            background=INK, color=PAPER,
            padding=".6rem 1rem", font_size=".85rem", border_radius="2px",
            max_width="82%",
        ),
        rx.box(
            message.text,
            align_self="flex-start",
            background=PAPER2, color=INK2,
            padding=".6rem 1rem", font_size=".85rem", border_radius="2px",
            border=f"1px solid {LINE}", line_height="1.6",
            max_width="82%",
        ),
    )


def ai_chat() -> rx.Component:
    return rx.box(
        # Section header
        rx.flex(
            rx.text("03", font_family="'Syne',sans-serif", font_size=".75rem",
                    color="#c94a2a", letter_spacing=".1em"),
            rx.heading("Ask About Tijil", font_family="'Syne',sans-serif", font_size="2rem",
                       font_weight="700", letter_spacing="-.02em", color=INK, as_="h2"),
            rx.box(flex="1", height="1px", background=LINE),
            align_items="baseline", gap="1.5rem", margin_bottom="2rem",
            class_name="reveal",
        ),
        rx.text(
            "Have questions about my experience, skills, or projects? "
            "Ask the AI assistant below — it knows my entire background.",
            color=INK2, font_size=".9rem", margin_bottom="2rem", max_width="480px",
            class_name="reveal",
        ),
        # Chat box
        rx.box(
            # Header
            rx.flex(
                rx.box(class_name="chat-dot"),
                rx.box(
                    rx.text("Portfolio Assistant", font_size=".8rem", font_weight="500", letter_spacing=".03em"),
                    rx.text("Powered by Claude · Ask anything about Tijil",
                            font_size=".7rem", color=INK3),
                ),
                align_items="center", gap=".75rem",
                padding="1rem 1.5rem", border_bottom=f"1px solid {LINE}",
            ),
            # Messages
            rx.flex(
                rx.foreach(State.messages, chat_bubble),
                rx.cond(
                    State.chat_loading,
                    rx.box(
                        "Thinking…",
                        align_self="flex-start",
                        background=PAPER2, color=INK3,
                        padding=".6rem 1rem", font_size=".85rem",
                        border_radius="2px", border=f"1px solid {LINE}",
                        font_style="italic", max_width="82%",
                    ),
                    rx.fragment(),
                ),
                direction="column", gap="1rem",
                height="300px", overflow_y="auto",
                padding="1.5rem", class_name="chat-messages",
                id="chat-messages",
            ),
            # Quick suggestions
            rx.flex(
                *[
                    rx.el.button(
                        s,
                        class_name="suggest-btn",
                        on_click=State.send_suggestion(s),
                        disabled=State.chat_loading,
                    )
                    for s in SUGGESTIONS
                ],
                flex_wrap="wrap", gap=".4rem",
                padding=".6rem 1.5rem", border_top=f"1px solid {LINE}",
            ),
            # Input row
            rx.flex(
                rx.el.input(
                    placeholder="Ask about experience, projects, skills…",
                    value=State.chat_input,
                    on_change=State.set_chat_input,
                    on_key_down=lambda e: rx.cond(e == "Enter", State.send_message(), rx.noop()),
                    disabled=State.chat_loading,
                    style={
                        "flex": "1", "border": "none", "background": "transparent",
                        "padding": ".9rem 1.5rem", "font_family": "'DM Sans',sans-serif",
                        "font_size": ".9rem", "color": INK, "outline": "none",
                    },
                ),
                rx.el.button(
                    "Send →",
                    on_click=State.send_message(),
                    disabled=State.chat_loading,
                    style={
                        "border": "none", "border_left": f"1px solid {LINE}",
                        "background": INK, "color": PAPER,
                        "padding": "0 1.5rem", "cursor": "pointer",
                        "font_size": ".85rem", "letter_spacing": ".04em",
                        "font_family": "'DM Sans',sans-serif",
                        "transition": "background .2s",
                        "opacity": rx.cond(State.chat_loading, "0.6", "1"),
                    },
                ),
                border_top=f"1px solid {LINE}",
            ),
            max_width="700px", margin="0 auto",
            border=f"1px solid {LINE}", background=PAPER,
            class_name="reveal",
        ),
        id="ai-section",
        background=PAPER2, border_top=f"1px solid {LINE}",
        padding="5rem 3rem",
    )
