"""Custom CSS for responsive design and styling."""


def get_global_styles() -> str:
    """Return global CSS styles for the entire app."""
    return """
    <style>
    /* ---- Global Reset & Typography ---- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Merriweather:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Merriweather', serif !important;
    }

    /* ---- Hero Section ---- */
    .hero-container {
        text-align: center;
        padding: 2rem 1rem 3rem;
    }

    .hero-title {
        font-family: 'Merriweather', serif !important;
        font-size: 3.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #4A90D9, #9B59B6, #E74C3C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #B0B8C8;
        font-weight: 300;
        margin-bottom: 2rem;
        font-style: italic;
    }

    .hero-tagline {
        font-size: 1.05rem;
        color: #8892A0;
        max-width: 600px;
        margin: 0 auto 2rem;
        line-height: 1.7;
    }

    /* ---- Feature Cards ---- */
    .feature-card {
        background: linear-gradient(145deg, #1A1F2E, #232940);
        border: 1px solid #2A3040;
        border-radius: 12px;
        padding: 1.8rem;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(74, 144, 217, 0.15);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.8rem;
    }

    .feature-title {
        font-family: 'Merriweather', serif !important;
        font-size: 1.2rem;
        font-weight: 600;
        color: #FAFAFA;
        margin-bottom: 0.5rem;
    }

    .feature-desc {
        font-size: 0.9rem;
        color: #8892A0;
        line-height: 1.5;
    }

    /* ---- Chapter Reader ---- */
    .chapter-content {
        font-family: 'Merriweather', serif !important;
        font-size: 1.1rem;
        line-height: 1.9;
        color: #D4D8E0;
        max-width: 720px;
        margin: 0 auto;
        padding: 1.5rem;
    }

    .chapter-heading {
        font-family: 'Merriweather', serif !important;
        font-size: 2rem;
        font-weight: 700;
        color: #FAFAFA;
        margin-bottom: 0.3rem;
        text-align: center;
    }

    .chapter-number {
        text-align: center;
        font-size: 0.9rem;
        color: #4A90D9;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 0.5rem;
    }

    .chapter-divider {
        text-align: center;
        color: #4A90D9;
        margin: 1rem 0 2rem;
        font-size: 1.2rem;
        letter-spacing: 8px;
    }

    /* ---- Summary Cards ---- */
    .summary-card {
        background: linear-gradient(145deg, #1A1F2E, #232940);
        border: 1px solid #2A3040;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .summary-card h4 {
        color: #4A90D9;
        margin-bottom: 0.5rem;
    }

    .takeaway-item {
        background: #1E2435;
        border-left: 3px solid #4A90D9;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.95rem;
        color: #C0C8D8;
    }

    /* ---- Quiz Styles ---- */
    .quiz-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(145deg, #1A1F2E, #232940);
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border: 1px solid #2A3040;
    }

    .score-display {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4A90D9;
    }

    .quiz-option {
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        margin: 0.4rem 0;
        cursor: pointer;
    }

    .correct-answer {
        background-color: rgba(46, 204, 113, 0.15) !important;
        border: 1px solid #2ECC71 !important;
    }

    .wrong-answer {
        background-color: rgba(231, 76, 60, 0.15) !important;
        border: 1px solid #E74C3C !important;
    }

    /* ---- AI Chat ---- */
    .ai-mode-card {
        background: linear-gradient(145deg, #1A1F2E, #232940);
        border: 1px solid #2A3040;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .ai-mode-card:hover {
        border-color: #4A90D9;
        box-shadow: 0 4px 16px rgba(74, 144, 217, 0.2);
    }

    /* ---- Section Headers ---- */
    .section-header {
        font-family: 'Merriweather', serif !important;
        font-size: 1.8rem;
        font-weight: 700;
        color: #FAFAFA;
        margin-bottom: 0.5rem;
    }

    .section-subheader {
        font-size: 1rem;
        color: #8892A0;
        margin-bottom: 2rem;
    }

    /* ---- Progress Bar ---- */
    .reading-progress {
        height: 4px;
        background: #1A1F2E;
        border-radius: 2px;
        margin: 1rem 0;
    }

    .reading-progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #4A90D9, #9B59B6);
        border-radius: 2px;
        transition: width 0.3s ease;
    }

    /* ---- Responsive Design ---- */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.2rem;
        }

        .hero-subtitle {
            font-size: 1.1rem;
        }

        .hero-tagline {
            font-size: 0.95rem;
        }

        .chapter-content {
            font-size: 1rem;
            padding: 1rem 0.5rem;
        }

        .chapter-heading {
            font-size: 1.6rem;
        }

        .feature-card {
            padding: 1.2rem;
        }
    }

    @media (max-width: 480px) {
        .hero-title {
            font-size: 1.8rem;
        }

        .hero-subtitle {
            font-size: 1rem;
        }

        .chapter-content {
            font-size: 0.95rem;
            line-height: 1.7;
        }
    }

    /* ---- Sidebar Styling ---- */
    [data-testid="stSidebar"] {
        background-color: #0E1117;
        border-right: 1px solid #1A1F2E;
    }

    /* ---- Button Overrides ---- */
    .stButton > button {
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
    }

    /* ---- Divider ---- */
    .styled-divider {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #2A3040, transparent);
        margin: 2rem 0;
    }
    </style>
    """
