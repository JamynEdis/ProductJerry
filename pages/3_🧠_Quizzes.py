"""Interactive quiz page for The Fifth Horseman."""

import streamlit as st

from utils.content import BOOK_TITLE, CHAPTERS
from utils.quiz_data import QUIZZES
from utils.styles import get_global_styles

st.set_page_config(
    page_title=f"Quizzes | {BOOK_TITLE}",
    page_icon="🧠",
    layout="wide",
)

st.markdown(get_global_styles(), unsafe_allow_html=True)

# ---- Initialize State ----
if "quiz_chapter" not in st.session_state:
    st.session_state["quiz_chapter"] = 1
if "quiz_answers" not in st.session_state:
    st.session_state["quiz_answers"] = {}
if "quiz_submitted" not in st.session_state:
    st.session_state["quiz_submitted"] = {}
if "quiz_scores" not in st.session_state:
    st.session_state["quiz_scores"] = {}

# ---- Header ----
st.markdown(
    '<div class="section-header" style="text-align:center;">Test Your Knowledge</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subheader" style="text-align:center;">'
    "Interactive quizzes on each chapter's key ideas</div>",
    unsafe_allow_html=True,
)

# ---- Chapter Selection ----
chapter_options = {f"Chapter {n}: {CHAPTERS[n]['title']}": n for n in QUIZZES}
selected_label = st.selectbox(
    "Select a chapter to quiz on",
    list(chapter_options.keys()),
    index=st.session_state["quiz_chapter"] - 1,
)
chapter_num = chapter_options[selected_label]
st.session_state["quiz_chapter"] = chapter_num

quiz = QUIZZES[chapter_num]
quiz_key = f"ch_{chapter_num}"
is_submitted = st.session_state["quiz_submitted"].get(quiz_key, False)

# ---- Score Display ----
if quiz_key in st.session_state["quiz_scores"]:
    score = st.session_state["quiz_scores"][quiz_key]
    total = len(quiz["questions"])
    pct = int((score / total) * 100)

    if pct == 100:
        grade_color = "#2ECC71"
        grade_msg = "Perfect score!"
    elif pct >= 67:
        grade_color = "#4A90D9"
        grade_msg = "Well done!"
    else:
        grade_color = "#E74C3C"
        grade_msg = "Keep reading!"

    st.markdown(
        f"""
        <div class="quiz-header">
            <div class="score-display" style="color:{grade_color};">{score}/{total}</div>
            <div style="color:{grade_color}; font-size:1.1rem;">{grade_msg}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---- Questions ----
st.markdown(f"### {quiz['title']}")

for i, q in enumerate(quiz["questions"]):
    q_key = f"{quiz_key}_q{i}"

    st.markdown(f"**Question {i + 1}:** {q['question']}")

    # Show options as radio
    selected = st.radio(
        f"q{i + 1}",
        q["options"],
        key=f"radio_{q_key}",
        index=st.session_state["quiz_answers"].get(q_key),
        label_visibility="collapsed",
        disabled=is_submitted,
    )

    # Store answer
    if selected is not None:
        st.session_state["quiz_answers"][q_key] = q["options"].index(selected)

    # Show feedback if submitted
    if is_submitted:
        user_answer = st.session_state["quiz_answers"].get(q_key)
        if user_answer == q["correct"]:
            st.success(f"Correct! {q['explanation']}")
        else:
            st.error(
                f"Incorrect. The answer is: **{q['options'][q['correct']]}**\n\n"
                f"{q['explanation']}"
            )

    st.markdown("---")

# ---- Submit / Reset ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if not is_submitted:
        if st.button("Submit Answers", use_container_width=True, type="primary"):
            # Calculate score
            score = 0
            for i, q in enumerate(quiz["questions"]):
                q_key = f"{quiz_key}_q{i}"
                if st.session_state["quiz_answers"].get(q_key) == q["correct"]:
                    score += 1

            st.session_state["quiz_scores"][quiz_key] = score
            st.session_state["quiz_submitted"][quiz_key] = True
            st.rerun()
    else:
        if st.button("Retake Quiz", use_container_width=True):
            # Clear answers for this chapter
            for i in range(len(quiz["questions"])):
                q_key = f"{quiz_key}_q{i}"
                st.session_state["quiz_answers"].pop(q_key, None)
            st.session_state["quiz_submitted"][quiz_key] = False
            st.session_state["quiz_scores"].pop(quiz_key, None)
            st.rerun()

# ---- Overall Progress ----
st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)
st.markdown("### Your Quiz Progress")

progress_cols = st.columns(len(QUIZZES))
for i, (num, q) in enumerate(QUIZZES.items()):
    with progress_cols[i]:
        qk = f"ch_{num}"
        if qk in st.session_state["quiz_scores"]:
            s = st.session_state["quiz_scores"][qk]
            t = len(q["questions"])
            st.metric(f"Ch. {num}", f"{s}/{t}")
        else:
            st.metric(f"Ch. {num}", "---")
