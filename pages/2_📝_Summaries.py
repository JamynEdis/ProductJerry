"""Chapter summaries page for The Fifth Horseman."""

import streamlit as st

from utils.content import BOOK_TITLE, CHAPTERS
from utils.styles import get_global_styles

st.set_page_config(
    page_title=f"Summaries | {BOOK_TITLE}",
    page_icon="📝",
    layout="wide",
)

st.markdown(get_global_styles(), unsafe_allow_html=True)

# ---- Header ----
st.markdown(
    '<div class="section-header" style="text-align:center;">Chapter Summaries</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subheader" style="text-align:center;">'
    "Key ideas and takeaways from each chapter</div>",
    unsafe_allow_html=True,
)

# ---- View Mode Toggle ----
view_mode = st.radio(
    "View",
    ["All Chapters", "Single Chapter"],
    horizontal=True,
    label_visibility="collapsed",
)

if view_mode == "Single Chapter":
    chapter_options = {f"Chapter {n}: {c['title']}": n for n, c in CHAPTERS.items()}
    selected_label = st.selectbox("Select a chapter", list(chapter_options.keys()))
    chapters_to_show = {chapter_options[selected_label]: CHAPTERS[chapter_options[selected_label]]}
else:
    chapters_to_show = CHAPTERS

# ---- Summaries ----
for num, chapter in chapters_to_show.items():
    st.markdown(
        f"""
        <div class="summary-card">
            <h4>Chapter {num}: {chapter["title"]}</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(chapter["summary"])

    st.markdown("**Key Takeaways:**")
    for takeaway in chapter["takeaways"]:
        st.markdown(
            f'<div class="takeaway-item">{takeaway}</div>',
            unsafe_allow_html=True,
        )

    # Quick actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"Read Full Chapter {num}", key=f"read_{num}", use_container_width=True):
            st.session_state["selected_chapter"] = num
            st.switch_page("pages/1_📖_Chapters.py")
    with col2:
        if st.button(f"Quiz on Chapter {num}", key=f"quiz_{num}", use_container_width=True):
            st.session_state["quiz_chapter"] = num
            st.switch_page("pages/3_🧠_Quizzes.py")

    st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)
