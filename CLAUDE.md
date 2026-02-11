# CLAUDE.md - AI Assistant Guide for ProductJerry

## Project Overview

ProductJerry is a Streamlit web application built from the official blank app template. It uses Python and the Streamlit framework for building interactive data-driven web apps.

- **Language**: Python (3.11+)
- **Framework**: Streamlit
- **License**: Apache 2.0
- **Deployment target**: Streamlit Community Cloud

## Repository Structure

```
ProductJerry/
├── .devcontainer/
│   └── devcontainer.json    # Dev container config (Python 3.11, VS Code extensions)
├── .github/
│   └── CODEOWNERS           # Code ownership (@streamlit/community-cloud)
├── streamlit_app.py         # Main application entry point
├── requirements.txt         # Python dependencies (pip)
├── README.md                # Project documentation
├── CLAUDE.md                # This file
├── .gitignore               # Python/Streamlit gitignore
└── LICENSE                  # Apache 2.0
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

### Run in dev container mode (CORS/XSRF disabled for local dev)
```
streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
```

The app runs on **port 8501** by default.

## Dependencies

Runtime dependencies are declared in `requirements.txt`. Currently only `streamlit` (unpinned).

## Key Files

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Main app entry point. All Streamlit UI code goes here. |
| `requirements.txt` | pip dependencies. Add new packages here. |
| `.devcontainer/devcontainer.json` | Dev container setup for Codespaces/VS Code. |

## Conventions

- **Entry point**: `streamlit_app.py` is the recognized Streamlit entry point filename.
- **Dependencies**: Add to `requirements.txt`, no version pinning currently used.
- **Secrets**: Use `.streamlit/secrets.toml` for local secrets (gitignored). Access via `st.secrets`.
- **No test framework**: No tests, linting, or CI/CD pipelines are configured yet.
- **No build step**: Python interpreted execution; no compilation required.

## Architecture Notes

This is currently a single-file Streamlit app. As the project grows, common patterns include:
- Adding `pages/` directory for multi-page Streamlit apps
- Adding `utils/` or `lib/` for shared helper modules
- Adding `.streamlit/config.toml` for Streamlit configuration
- Adding `packages.txt` for system-level apt dependencies (used by devcontainer and Streamlit Cloud)

## Deployment

The app is designed for Streamlit Community Cloud deployment. Push to the repository and connect via [share.streamlit.io](https://share.streamlit.io). The platform reads `requirements.txt` and runs `streamlit_app.py` automatically.
