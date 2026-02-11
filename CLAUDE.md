# CLAUDE.md - AI Assistant Guide for ProductJerry

## Project Overview

ProductJerry is an interactive Streamlit web application for **"The Fifth Horseman"** by Jamyn Edis. It serves as both a marketing site and an immersive reading experience, combining chapter reading, summaries, quizzes, and AI-powered conversations.

- **Language**: Python (3.11+)
- **Framework**: Streamlit (multi-page app)
- **License**: Apache 2.0
- **Deployment target**: Streamlit Community Cloud

## Repository Structure

```
ProductJerry/
├── .devcontainer/
│   └── devcontainer.json          # Dev container config (Python 3.11)
├── .github/
│   └── CODEOWNERS                 # Code ownership
├── .streamlit/
│   └── config.toml                # Streamlit theme (dark mode, colors, fonts)
├── pages/
│   ├── 1_📖_Chapters.py          # Chapter reader with progress tracking
│   ├── 2_📝_Summaries.py         # Chapter summaries and key takeaways
│   ├── 3_🧠_Quizzes.py           # Interactive multiple-choice quizzes
│   └── 4_🤖_AI_Experience.py     # AI chat (ask the book, characters, themes)
├── utils/
│   ├── __init__.py
│   ├── content.py                 # Book content, chapters, characters, themes
│   ├── quiz_data.py               # Quiz questions and answers per chapter
│   └── styles.py                  # Global CSS (responsive, typography, cards)
├── streamlit_app.py               # Home/landing page (entry point)
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── CLAUDE.md                      # This file
├── .gitignore                     # Python/Streamlit gitignore
└── LICENSE                        # Apache 2.0
```

## Development Commands

### Install dependencies
```
pip install -r requirements.txt
```

### Run the application
```
streamlit run streamlit_app.py
```

### Run in dev container mode (CORS/XSRF disabled)
```
streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
```

The app runs on **port 8501** by default.

## Dependencies

- `streamlit` - Web framework
- `anthropic` - AI chat features (optional; app works without API key)

## Architecture

### Multi-Page Streamlit App
- **`streamlit_app.py`**: Home/landing page with hero section, synopsis, feature cards, chapter previews, and author bio.
- **`pages/`**: Each file is an auto-registered Streamlit page. Naming convention `N_emoji_Name.py` controls sidebar order.

### Content Layer (`utils/`)
- **`content.py`**: All book text, metadata, chapter content, summaries, takeaways, character profiles, and themes. Edit this file to update book content.
- **`quiz_data.py`**: Quiz questions per chapter with options, correct answers, and explanations.
- **`styles.py`**: Single source of CSS. Uses responsive breakpoints (768px, 480px), custom fonts (Inter + Merriweather), and gradient styling.

### AI Experience
- Supports three modes: Ask the Book, Character Chat, Theme Explorer
- Uses Anthropic API when `ANTHROPIC_API_KEY` is set in `.streamlit/secrets.toml`
- Falls back to built-in content-matching responses when no API key is configured
- System prompts are dynamically built from book content (`build_system_prompt()`)

### State Management
- Uses `st.session_state` for: selected chapter, chapters read, quiz answers/scores, AI chat messages, selected character
- State persists across page navigations within a session

## Key Conventions

- **Entry point**: `streamlit_app.py` (Streamlit convention)
- **Page files**: `pages/N_emoji_Name.py` format for auto-ordering
- **All book content** lives in `utils/content.py` - single source of truth
- **All quiz data** lives in `utils/quiz_data.py` - one quiz per chapter
- **CSS**: All styles in `utils/styles.py`, injected via `st.markdown(get_global_styles(), unsafe_allow_html=True)`
- **Secrets**: Use `.streamlit/secrets.toml` for API keys (gitignored)
- **No test framework**: No tests or CI/CD configured yet

## How to Modify

| Task | File(s) to Edit |
|------|-----------------|
| Change book content | `utils/content.py` |
| Add/edit quiz questions | `utils/quiz_data.py` |
| Update visual design | `utils/styles.py` |
| Modify landing page | `streamlit_app.py` |
| Change AI behavior | `pages/4_🤖_AI_Experience.py` |
| Add a new page | Create `pages/N_emoji_Name.py` |
| Configure theme colors | `.streamlit/config.toml` |

## Deployment

Deploy to Streamlit Community Cloud at [share.streamlit.io](https://share.streamlit.io). The platform reads `requirements.txt` and runs `streamlit_app.py` automatically. For AI features, configure `ANTHROPIC_API_KEY` in the Streamlit Cloud secrets manager.
