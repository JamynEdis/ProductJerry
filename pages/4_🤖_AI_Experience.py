"""AI-powered interactive experience for The Fifth Horseman."""

import streamlit as st

from utils.content import BOOK_TITLE, BOOK_THEMES, CHAPTERS, CHARACTERS
from utils.styles import get_global_styles

st.set_page_config(
    page_title=f"AI Experience | {BOOK_TITLE}",
    page_icon="🤖",
    layout="wide",
)

st.markdown(get_global_styles(), unsafe_allow_html=True)

# ---- Initialize State ----
if "ai_mode" not in st.session_state:
    st.session_state["ai_mode"] = None
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []
if "selected_character" not in st.session_state:
    st.session_state["selected_character"] = None


def get_book_context() -> str:
    """Build a context string from the book content for AI responses."""
    context_parts = []
    for num, ch in CHAPTERS.items():
        context_parts.append(
            f"Chapter {num} - {ch['title']}:\n"
            f"Summary: {ch['summary']}\n"
            f"Key Takeaways: {', '.join(ch['takeaways'])}\n"
        )
    return "\n".join(context_parts)


def build_system_prompt(mode: str, character: str | None = None) -> str:
    """Build a system prompt based on the selected AI mode."""
    book_context = get_book_context()

    if mode == "ask":
        return (
            f"You are a knowledgeable assistant for the book '{BOOK_TITLE}'. "
            f"Answer questions using the following book content:\n\n{book_context}\n\n"
            "Be thoughtful and reference specific chapters when relevant. "
            "If asked about something not covered in the book, say so honestly."
        )
    elif mode == "character" and character and character in CHARACTERS:
        char = CHARACTERS[character]
        return (
            f"You are roleplaying as '{character}' from the book '{BOOK_TITLE}'.\n"
            f"Description: {char['description']}\n"
            f"Personality: {char['personality']}\n\n"
            f"Book context:\n{book_context}\n\n"
            "Stay in character. Draw on the book's themes and ideas in your responses. "
            "Be engaging and thought-provoking."
        )
    elif mode == "themes":
        themes_str = "\n".join(f"- {t}" for t in BOOK_THEMES)
        return (
            f"You are a literary discussion facilitator for '{BOOK_TITLE}'.\n"
            f"Key themes:\n{themes_str}\n\n"
            f"Book context:\n{book_context}\n\n"
            "Help the reader explore and discuss the book's themes. Ask thought-provoking "
            "questions. Connect ideas across chapters. Encourage critical thinking."
        )
    return ""


def generate_response(messages: list, system_prompt: str) -> str:
    """Generate a response using the configured AI provider.

    Attempts to use the Anthropic API if a key is configured.
    Falls back to a helpful built-in response otherwise.
    """
    api_key = st.secrets.get("ANTHROPIC_API_KEY", "")

    if api_key:
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=api_key)
            api_messages = [
                {"role": m["role"], "content": m["content"]} for m in messages
            ]
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1024,
                system=system_prompt,
                messages=api_messages,
            )
            return response.content[0].text
        except Exception as e:
            return f"*AI service error: {e}*\n\nPlease check your API key configuration."

    # Built-in responses when no API key is configured
    return _builtin_response(messages, system_prompt)


def _builtin_response(messages: list, system_prompt: str) -> str:
    """Provide built-in responses based on book content when no AI API is available."""
    last_msg = messages[-1]["content"].lower() if messages else ""

    # Match against book content for relevant responses
    for num, ch in CHAPTERS.items():
        if ch["title"].lower() in last_msg or f"chapter {num}" in last_msg:
            return (
                f"**Chapter {num}: {ch['title']}**\n\n"
                f"{ch['summary']}\n\n"
                f"**Key takeaways:**\n"
                + "\n".join(f"- {t}" for t in ch["takeaways"])
                + "\n\n*Connect an AI API key in `.streamlit/secrets.toml` "
                "for deeper, dynamic conversations.*"
            )

    # Theme-based responses
    for theme in BOOK_THEMES:
        keywords = theme.lower().split()
        if any(kw in last_msg for kw in keywords if len(kw) > 4):
            return (
                f'The theme of **"{theme}"** runs throughout the book.\n\n'
                "The author argues that understanding this requires looking at both "
                "the historical patterns of disruption and the unique nature of AI as "
                "a force that creates as much as it destroys.\n\n"
                "*Connect an AI API key for richer, dynamic conversations about this theme.*"
            )

    # Default response
    return (
        "That's a great question to explore! The Fifth Horseman touches on many "
        "interconnected ideas about technology, humanity, and choice.\n\n"
        "Try asking about:\n"
        "- A specific chapter (e.g., *'Tell me about Chapter 3'*)\n"
        "- Key themes (e.g., *'What does the book say about agency?'*)\n"
        "- The horseman metaphor (e.g., *'Why a fifth horseman?'*)\n\n"
        "**To unlock full AI-powered conversations**, add your Anthropic API key "
        "to `.streamlit/secrets.toml`:\n"
        "```toml\n"
        'ANTHROPIC_API_KEY = "your-key-here"\n'
        "```"
    )


# ---- Header ----
st.markdown(
    '<div class="section-header" style="text-align:center;">AI Experience</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subheader" style="text-align:center;">'
    "Interact with the book through AI-powered conversations</div>",
    unsafe_allow_html=True,
)

# ---- Mode Selection ----
if st.session_state["ai_mode"] is None:
    st.markdown("### Choose your experience")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="ai-mode-card">
                <div style="font-size:2.5rem;">💬</div>
                <div style="font-size:1.1rem; font-weight:600; margin:0.5rem 0;">Ask the Book</div>
                <div style="font-size:0.9rem; color:#8892A0;">
                    Ask questions about the content, themes, and ideas in The Fifth Horseman.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Start Asking", key="mode_ask", use_container_width=True):
            st.session_state["ai_mode"] = "ask"
            st.session_state["chat_messages"] = []
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="ai-mode-card">
                <div style="font-size:2.5rem;">🎭</div>
                <div style="font-size:1.1rem; font-weight:600; margin:0.5rem 0;">Chat with Characters</div>
                <div style="font-size:0.9rem; color:#8892A0;">
                    Have a conversation with characters and voices from the book.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Meet Characters", key="mode_char", use_container_width=True):
            st.session_state["ai_mode"] = "character"
            st.session_state["chat_messages"] = []
            st.rerun()

    with col3:
        st.markdown(
            """
            <div class="ai-mode-card">
                <div style="font-size:2.5rem;">🔍</div>
                <div style="font-size:1.1rem; font-weight:600; margin:0.5rem 0;">Explore Themes</div>
                <div style="font-size:0.9rem; color:#8892A0;">
                    Dive deep into the book's themes with a guided AI discussion.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore Themes", key="mode_themes", use_container_width=True):
            st.session_state["ai_mode"] = "themes"
            st.session_state["chat_messages"] = []
            st.rerun()

    # API Key status
    st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)
    api_key = st.secrets.get("ANTHROPIC_API_KEY", "")
    if api_key:
        st.success("Anthropic API key configured. Full AI experience available.")
    else:
        st.info(
            "**No API key configured.** The AI experience works with built-in responses. "
            "For full AI-powered conversations, add your Anthropic API key to "
            "`.streamlit/secrets.toml`."
        )

else:
    # ---- Active Chat Mode ----
    mode = st.session_state["ai_mode"]

    # Mode header and back button
    mode_labels = {
        "ask": "💬 Ask the Book",
        "character": "🎭 Character Chat",
        "themes": "🔍 Theme Explorer",
    }

    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"### {mode_labels.get(mode, 'AI Chat')}")
    with col2:
        if st.button("← Back", use_container_width=True):
            st.session_state["ai_mode"] = None
            st.session_state["chat_messages"] = []
            st.session_state["selected_character"] = None
            st.rerun()

    # Character selection for character mode
    if mode == "character":
        if st.session_state["selected_character"] is None:
            st.markdown("**Select a character to talk with:**")
            char_cols = st.columns(len(CHARACTERS))
            for i, (name, info) in enumerate(CHARACTERS.items()):
                with char_cols[i]:
                    st.markdown(f"**{name}**")
                    st.markdown(f"*{info['description']}*")
                    if st.button(f"Chat with {name}", key=f"char_{i}", use_container_width=True):
                        st.session_state["selected_character"] = name
                        st.session_state["chat_messages"] = [
                            {
                                "role": "assistant",
                                "content": f"*{name} appears before you.*\n\n"
                                f"{info['description']}\n\nWhat would you like to discuss?",
                            }
                        ]
                        st.rerun()
        else:
            st.markdown(f"*Chatting with **{st.session_state['selected_character']}***")

    # Opening messages for non-character modes
    if mode == "ask" and not st.session_state["chat_messages"]:
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "content": (
                    "Welcome! I'm here to help you explore **The Fifth Horseman**. "
                    "Ask me anything about the book's content, themes, or ideas.\n\n"
                    "Try questions like:\n"
                    "- *What is the Fifth Horseman?*\n"
                    "- *What happens in Chapter 3?*\n"
                    "- *What does the author think about AI?*"
                ),
            }
        ]
    elif mode == "themes" and not st.session_state["chat_messages"]:
        themes_list = "\n".join(f"- {t}" for t in BOOK_THEMES[:4])
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "content": (
                    "Let's explore the themes of **The Fifth Horseman** together. "
                    "Some key themes include:\n\n"
                    f"{themes_list}\n\n"
                    "Which theme interests you most? Or ask me to connect ideas across chapters."
                ),
            }
        ]

    # Render chat
    if st.session_state["chat_messages"] or (
        mode == "character" and st.session_state["selected_character"]
    ):
        for msg in st.session_state["chat_messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Chat input
        if prompt := st.chat_input("Type your message..."):
            st.session_state["chat_messages"].append(
                {"role": "user", "content": prompt}
            )

            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            system_prompt = build_system_prompt(
                mode, st.session_state.get("selected_character")
            )

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response(
                        st.session_state["chat_messages"], system_prompt
                    )
                st.markdown(response)

            st.session_state["chat_messages"].append(
                {"role": "assistant", "content": response}
            )
