"""Chapter reader page for The Fifth Horseman."""

import streamlit as st

from utils.content import BOOK_TITLE, CHAPTERS
from utils.styles import get_global_styles

st.set_page_config(
    page_title=f"Read | {BOOK_TITLE}",
    page_icon="📖",
    layout="wide",
)

st.markdown(get_global_styles(), unsafe_allow_html=True)

# ---- Initialize State ----
if "selected_chapter" not in st.session_state:
    st.session_state["selected_chapter"] = 1
if "chapters_read" not in st.session_state:
    st.session_state["chapters_read"] = set()

total_chapters = len(CHAPTERS)

# ---- Sidebar Navigation ----
with st.sidebar:
    st.markdown("### 📖 Chapters")
    st.markdown("---")

    for num, chapter in CHAPTERS.items():
        read_marker = " ✓" if num in st.session_state["chapters_read"] else ""
        if st.button(
            f"Ch. {num}: {chapter['title']}{read_marker}",
            key=f"nav_{num}",
            use_container_width=True,
            type="primary" if num == st.session_state["selected_chapter"] else "secondary",
        ):
            st.session_state["selected_chapter"] = num
            st.rerun()

    st.markdown("---")
    read_count = len(st.session_state["chapters_read"])
    st.markdown(f"**Progress:** {read_count}/{total_chapters} chapters")
    st.progress(read_count / total_chapters if total_chapters > 0 else 0)

# ---- Chapter Content ----
current = st.session_state["selected_chapter"]
chapter = CHAPTERS[current]

# Reading progress bar at top
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.markdown(
        f'<div class="chapter-number">Chapter {current} of {total_chapters}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="chapter-heading">{chapter["title"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="chapter-divider">~ ~ ~</div>',
        unsafe_allow_html=True,
    )

    # Render chapter content with proper paragraph formatting
    paragraphs = chapter["content"].split("\n\n")
    formatted = "".join(f"<p>{p}</p>" for p in paragraphs)
    st.markdown(
        f'<div class="chapter-content">{formatted}</div>',
        unsafe_allow_html=True,
    )

    # Mark as read
    st.session_state["chapters_read"].add(current)

    st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

    # ---- Navigation Buttons ----
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])

    with nav_col1:
        if current > 1:
            if st.button("← Previous Chapter", use_container_width=True):
                st.session_state["selected_chapter"] = current - 1
                st.rerun()

    with nav_col2:
        st.markdown(
            f'<div style="text-align:center; color:#5A6270; padding-top:0.5rem;">'
            f'Chapter {current} of {total_chapters}</div>',
            unsafe_allow_html=True,
        )

    with nav_col3:
        if current < total_chapters:
            if st.button("Next Chapter →", use_container_width=True):
                st.session_state["selected_chapter"] = current + 1
                st.rerun()
