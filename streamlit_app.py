"""The Fifth Horseman - Interactive Book Experience."""

import streamlit as st

from utils.content import (
    BOOK_AUTHOR,
    BOOK_SYNOPSIS,
    BOOK_TAGLINE,
    BOOK_TITLE,
    AUTHOR_BIO,
    CHAPTERS,
)
from utils.styles import get_global_styles

# ---- Page Config ----
st.set_page_config(
    page_title=f"{BOOK_TITLE} | {BOOK_AUTHOR}",
    page_icon="🐴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- Global Styles ----
st.markdown(get_global_styles(), unsafe_allow_html=True)

# ---- Sidebar ----
with st.sidebar:
    st.markdown(f"### 🐴 {BOOK_TITLE}")
    st.markdown(f"*by {BOOK_AUTHOR}*")
    st.markdown("---")
    st.markdown("**Navigate**")
    st.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.page_link("pages/1_📖_Chapters.py", label="Read Chapters", icon="📖")
    st.page_link("pages/2_📝_Summaries.py", label="Summaries", icon="📝")
    st.page_link("pages/3_🧠_Quizzes.py", label="Quizzes", icon="🧠")
    st.page_link("pages/4_🤖_AI_Experience.py", label="AI Experience", icon="🤖")

# ---- Hero Section ----
st.markdown(
    f"""
    <div class="hero-container">
        <div class="hero-title">{BOOK_TITLE}</div>
        <div class="hero-subtitle">by {BOOK_AUTHOR}</div>
        <div class="hero-tagline">{BOOK_TAGLINE}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- CTA Buttons ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("Start Reading", use_container_width=True, type="primary"):
            st.switch_page("pages/1_📖_Chapters.py")
    with btn_col2:
        if st.button("Try AI Experience", use_container_width=True):
            st.switch_page("pages/4_🤖_AI_Experience.py")

st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# ---- Synopsis ----
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(
        '<div class="section-header">About the Book</div>',
        unsafe_allow_html=True,
    )
    st.markdown(BOOK_SYNOPSIS)

st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# ---- Feature Cards ----
st.markdown(
    '<div class="section-header" style="text-align:center;">Experience the Book</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subheader" style="text-align:center;">Multiple ways to engage with The Fifth Horseman</div>',
    unsafe_allow_html=True,
)

features = [
    {
        "icon": "📖",
        "title": "Read Chapters",
        "desc": "Dive into the full text with a clean, distraction-free reading experience designed for deep engagement.",
        "page": "pages/1_📖_Chapters.py",
    },
    {
        "icon": "📝",
        "title": "Chapter Summaries",
        "desc": "Get key takeaways and summaries for each chapter. Perfect for review or a quick overview.",
        "page": "pages/2_📝_Summaries.py",
    },
    {
        "icon": "🧠",
        "title": "Test Your Knowledge",
        "desc": "Take interactive quizzes on each chapter to reinforce your understanding of the core ideas.",
        "page": "pages/3_🧠_Quizzes.py",
    },
    {
        "icon": "🤖",
        "title": "AI Experience",
        "desc": "Chat with characters from the book, ask questions about the content, and explore themes with AI.",
        "page": "pages/4_🤖_AI_Experience.py",
    },
]

cols = st.columns(4)
for i, feature in enumerate(features):
    with cols[i]:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{feature["icon"]}</div>
                <div class="feature-title">{feature["title"]}</div>
                <div class="feature-desc">{feature["desc"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore", key=f"feat_{i}", use_container_width=True):
            st.switch_page(feature["page"])

st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# ---- Chapter Preview ----
st.markdown(
    '<div class="section-header" style="text-align:center;">Inside the Book</div>',
    unsafe_allow_html=True,
)

for num, chapter in CHAPTERS.items():
    with st.expander(f"Chapter {num}: {chapter['title']}"):
        st.markdown(f"*{chapter['summary']}*")
        if st.button(f"Read Chapter {num}", key=f"read_{num}"):
            st.session_state["selected_chapter"] = num
            st.switch_page("pages/1_📖_Chapters.py")

st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# ---- Author Section ----
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(
        '<div class="section-header">About the Author</div>',
        unsafe_allow_html=True,
    )
    st.markdown(AUTHOR_BIO)

# ---- Footer ----
st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="text-align:center; color:#5A6270; font-size:0.85rem; padding:1rem;">
        <em>{BOOK_TITLE}</em> &copy; {BOOK_AUTHOR} &middot; All rights reserved
    </div>
    """,
    unsafe_allow_html=True,
)
