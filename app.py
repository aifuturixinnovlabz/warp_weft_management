import streamlit as st
import pandas as pd
from datetime import date, timedelta
from database import Database
from backend import MaterialService

# ========================================
# STRICT LIGHT THEME CONFIGURATION
# ========================================
st.set_page_config(
    page_title="WARP & WEFT Management",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "WARP & WEFT Management System"
    }
)

# Initialize
if 'db' not in st.session_state:
    st.session_state.db = Database()
    st.session_state.service = MaterialService(st.session_state.db)

# ========================================
# COMPREHENSIVE LIGHT THEME CSS
# ========================================
st.markdown("""
    <style>
    /* ========================================
       FORCE LIGHT THEME - ROOT VARIABLES
       ======================================== */
    :root {
        --primary-blue: #1976d2;
        --primary-blue-dark: #1565c0;
        --primary-blue-light: #42a5f5;
        --accent-teal: #00897b;
        --accent-teal-light: #26a69a;
        --bg-main: #f5f7fa;
        --surface-white: #ffffff;
        --text-primary: #263238;
        --text-dark: #1a1a1a;
        --border-light: #cfd8dc;
        --success-green: #43a047;
        --delete-red: #d32f2f;
    }

    /* Override Streamlit's theme detection */
    [data-testid="stAppViewContainer"],
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e3f2fd 100%) !important;
        color: var(--text-dark) !important;
    }

    /* Main content area */
    .main .block-container {
        background-color: transparent !important;
        color: var(--text-dark) !important;
    }
    /* ============================================
   CURSOR/CARET VISIBILITY FIX
   ============================================ */

/* Text Input Cursor */
.stTextInput input,
input[type="text"],
[data-baseweb="input"] input[type="text"] {
    caret-color: var(--primary-blue) !important;  /* Blue cursor */
}

/* Number Input Cursor */
.stNumberInput input,
input[type="number"],
[data-baseweb="input"] input[type="number"] {
    caret-color: var(--primary-blue) !important;  /* Blue cursor */
}

/* Text Area Cursor */
.stTextArea textarea,
textarea {
    caret-color: var(--primary-blue) !important;  /* Blue cursor */
}

/* Date Input Cursor */
.stDateInput input,
input[type="date"],
[data-baseweb="input"] input {
    caret-color: var(--primary-blue) !important;  /* Blue cursor */
}

/* All Input Fields - Universal Fix */
input, textarea, select {
    caret-color: var(--primary-blue) !important;  /* Blue cursor for all inputs */
}

/* Ensure text is visible when typing */
input::placeholder,
textarea::placeholder {
    color: #666666 !important;
    opacity: 0.7 !important;
}


    /* ========================================
       SIDEBAR STYLING
       ======================================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #e3f2fd 100%) !important;
        border-right: 2px solid #90caf9 !important;
    }

    [data-testid="stSidebar"] * {
        color: var(--text-dark) !important;
    }

    [data-testid="stSidebar"] .css-17lntkn {
        color: var(--text-dark) !important;
    }
    /* ========================================
   SIDEBAR COLLAPSE BUTTON & HEADER FIX
   ======================================== */

/* Sidebar collapse button (>>) */
[data-testid="collapsedControl"] {
    background-color: var(--primary-blue) !important;
    color: white !important;
    border: 2px solid var(--primary-blue-dark) !important;
    border-radius: 0 8px 8px 0 !important;
}

[data-testid="collapsedControl"]:hover {
    background-color: var(--primary-blue-dark) !important;
    box-shadow: 0 4px 12px rgba(25, 118, 210, 0.3) !important;
}

[data-testid="collapsedControl"] svg {
    color: white !important;
    fill: white !important;
}

/* Sidebar header (when collapsed) */
[data-testid="stSidebarNav"] {
    background-color: transparent !important;
}

/* Main header area */
header[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Toolbar/hamburger menu */
[data-testid="stToolbar"] {
    background-color: transparent !important;
}

[data-testid="stToolbar"] button {
    color: var(--primary-blue) !important;
}

[data-testid="stToolbar"] button:hover {
    background-color: #e3f2fd !important;
}

/* Hamburger menu icon */
[data-testid="stToolbar"] svg {
    color: var(--primary-blue) !important;
    fill: var(--primary-blue) !important;
}
    
    # Add this in the CSS section, after the SIDEBAR STYLING section (around line 70)

/* ========================================
   SIDEBAR RADIO - HIGHLIGHT SELECTED
   ======================================== */
[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label {
    background-color: transparent !important;
    padding: 12px 16px !important;
    border-radius: 8px !important;
    margin: 4px 0 !important;
    transition: all 0.3s ease !important;
    border: 2px solid transparent !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
    background-color: #e3f2fd !important;
    border: 2px solid #90caf9 !important;
}

/* Selected radio button - HIGHLIGHT */
[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-baseweb="radio"] > div[data-checked="true"],
[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input[type="radio"]:checked) {
    background: linear-gradient(135deg, #1976d2 0%, #42a5f5 100%) !important;
    border: 2px solid #1565c0 !important;
    box-shadow: 0 4px 12px rgba(25, 118, 210, 0.3) !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input[type="radio"]:checked) p,
[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input[type="radio"]:checked) span {
    color: white !important;
    font-weight: 700 !important;
}

/* Radio circle indicator */
[data-testid="stSidebar"] [data-testid="stRadio"] div[data-baseweb="radio"] > div:first-child {
    background-color: white !important;
    border: 2px solid var(--primary-blue) !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] div[data-baseweb="radio"][data-checked="true"] > div:first-child {
    background-color: white !important;
    border: 2px solid white !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] div[data-baseweb="radio"][data-checked="true"] > div:first-child::after {
    background-color: var(--primary-blue) !important;
}

    /* ========================================
       TYPOGRAPHY
       ======================================== */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #1976d2 0%, #00897b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px;
        margin-bottom: 20px;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--primary-blue-dark) !important;
        font-weight: 700 !important;
    }

    p, span, div, label, li, a {
        color: var(--text-dark) !important;
    }

    /* ========================================
       METRICS
       ======================================== */
    .stMetric {
        background: linear-gradient(135deg, #ffffff 0%, #e8f4f8 100%) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(25, 118, 210, 0.08) !important;
        border: 1px solid #b3e5fc !important;
    }

    .stMetric label {
        color: var(--primary-blue) !important;
        font-weight: 600 !important;
    }

    .stMetric [data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }

    .stMetric [data-testid="stMetricDelta"] {
        color: var(--text-dark) !important;
    }

    /* ========================================
       BUTTONS
       ======================================== */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, var(--primary-blue-light) 0%, var(--primary-blue) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(25, 118, 210, 0.2) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-blue-dark) 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(25, 118, 210, 0.3) !important;
    }

    .stButton>button:active {
        transform: translateY(0px) !important;
    }

    /* Secondary buttons */
    button[kind="secondary"],
    button[data-testid="baseButton-secondary"] {
        background: linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%) !important;
        color: var(--text-dark) !important;
        border: 1px solid var(--border-light) !important;
    }

    button[kind="secondary"]:hover,
    button[data-testid="baseButton-secondary"]:hover {
        background: linear-gradient(135deg, #e0e0e0 0%, #d5d5d5 100%) !important;
    }

    /* Form submit buttons */
    .stFormSubmitButton>button {
        background: linear-gradient(135deg, var(--accent-teal-light) 0%, var(--accent-teal) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 28px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 12px rgba(0, 137, 123, 0.25) !important;
        width: 100% !important;
    }

    .stFormSubmitButton>button:hover {
        background: linear-gradient(135deg, var(--accent-teal) 0%, #00695c 100%) !important;
        transform: translateY(-2px) !important;
    }

    /* Download buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #66bb6a 0%, var(--success-green) 100%) !important;
        color: white !important;
        padding: 12px 24px !important;
        border: none !important;
        border-radius: 10px !important;
    }

    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, var(--success-green) 0%, #2e7d32 100%) !important;
    }

    /* ========================================
       INPUT FIELDS - TEXT
       ======================================== */
    .stTextInput>div>div>input,
    .stTextInput input,
    input[type="text"],
    [data-baseweb="input"] input[type="text"] {
        background-color: #ffffff !important;
        border: 2px solid var(--border-light) !important;
        border-radius: 8px !important;
        color: var(--text-dark) !important;
        font-weight: 500 !important;
        padding: 10px 14px !important;
    }

    /* ========================================
       INPUT FIELDS - NUMBER
       ======================================== */
    .stNumberInput>div>div>input,
    .stNumberInput input,
    input[type="number"],
    [data-baseweb="input"] input[type="number"] {
        background-color: #ffffff !important;
        border: 2px solid var(--border-light) !important;
        border-radius: 8px !important;
        color: var(--text-dark) !important;
        font-weight: 500 !important;
        padding: 10px 14px !important;
    }

    /* Number input increment/decrement buttons */
    button[kind="icon"],
    button[aria-label*="Increment"],
    button[aria-label*="Decrement"] {
        background-color: #f5f5f5 !important;
        color: var(--text-dark) !important;
        border: 1px solid var(--border-light) !important;
    }

    button[kind="icon"]:hover {
        background-color: #e0e0e0 !important;
    }

    /* ========================================
       TEXT AREA
       ======================================== */
    .stTextArea>div>div>textarea,
    textarea {
        background-color: #ffffff !important;
        border: 2px solid var(--border-light) !important;
        border-radius: 8px !important;
        color: var(--text-dark) !important;
        font-weight: 500 !important;
        padding: 10px 14px !important;
    }

    /* ========================================
       DATE INPUT - COMPLETE FIX
       ======================================== */
    .stDateInput>div>div>input,
    .stDateInput input,
    input[type="date"],
    [data-baseweb="input"] input {
        background-color: #ffffff !important;
        border: 2px solid var(--border-light) !important;
        border-radius: 8px !important;
        color: var(--text-dark) !important;
        font-weight: 500 !important;
        padding: 10px 14px !important;
    }

    [data-baseweb="input"],
    [data-baseweb="base-input"] {
        background-color: #ffffff !important;
    }

    [data-baseweb="input"] > div,
    [data-baseweb="base-input"] > div {
        background-color: #ffffff !important;
    }

    /* ========================================
       DATE PICKER CALENDAR - COMPLETE OVERRIDE
       ======================================== */
    [data-baseweb="calendar"],
    [data-baseweb="popover"],
    [data-testid="stPopover"],
    div[role="dialog"] {
        background-color: #ffffff !important;
        border: 1px solid var(--border-light) !important;
        border-radius: 8px !important;
    }

    /* Calendar header */
    [data-baseweb="calendar"] header,
    [data-baseweb="calendar-header"] {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
        padding: 10px !important;
    }

    /* Calendar month/year controls */
    [data-baseweb="calendar"] button,
    [data-baseweb="calendar"] select {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
        border: 1px solid var(--border-light) !important;
        border-radius: 6px !important;
        padding: 6px 12px !important;
    }

    /* Calendar navigation arrows */
    [data-baseweb="calendar"] button[aria-label*="previous"],
    [data-baseweb="calendar"] button[aria-label*="next"] {
        background-color: #f5f5f5 !important;
        color: var(--text-dark) !important;
    }

    [data-baseweb="calendar"] button:hover {
        background-color: #e3f2fd !important;
        color: var(--text-dark) !important;
    }

    /* Calendar weekday headers */
    [data-baseweb="calendar"] thead th {
        background-color: #f5f5f5 !important;
        color: var(--text-dark) !important;
        font-weight: 600 !important;
        padding: 8px !important;
    }

    /* Calendar days */
    [data-baseweb="calendar"] [role="gridcell"],
    [data-baseweb="calendar"] td {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
    }

    [data-baseweb="calendar"] [role="gridcell"] > div {
        color: var(--text-dark) !important;
    }

    /* Selected day */
    [data-baseweb="calendar"] [aria-selected="true"],
    [data-baseweb="calendar"] td[aria-selected="true"] {
        background-color: var(--primary-blue) !important;
        color: white !important;
    }

    [data-baseweb="calendar"] [aria-selected="true"] > div {
        color: white !important;
    }

    /* Today */
    [data-baseweb="calendar"] [aria-current="date"] {
        background-color: #ffebee !important;
        color: var(--text-dark) !important;
        border: 2px solid #d32f2f !important;
    }

    /* Calendar hover */
    [data-baseweb="calendar"] [role="gridcell"]:hover,
    [data-baseweb="calendar"] td:hover {
        background-color: #e3f2fd !important;
        color: var(--text-dark) !important;
    }

    /* All calendar text */
    [data-baseweb="calendar"] *,
    [data-baseweb="calendar"] span,
    [data-baseweb="calendar"] div,
    [data-baseweb="calendar"] button {
        color: var(--text-dark) !important;
    }

    /* ========================================
       PLACEHOLDER TEXT
       ======================================== */
    input::placeholder,
    textarea::placeholder {
        color: #666666 !important;
        opacity: 0.7 !important;
    }

    /* ========================================
       FOCUS STATES
       ======================================== */
    input:focus,
    textarea:focus,
    select:focus {
        border-color: var(--primary-blue) !important;
        box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.15) !important;
        background-color: #ffffff !important;
        outline: none !important;
    }

    /* ========================================
       SELECT BOX / DROPDOWN
       ======================================== */
    .stSelectbox>div>div,
    [data-baseweb="select"] {
        background: var(--surface-white) !important;
        border: 2px solid var(--border-light) !important;
        border-radius: 8px !important;
    }

    .stSelectbox>div>div>div,
    [data-baseweb="select"] > div {
        color: var(--text-dark) !important;
        background: var(--surface-white) !important;
    }

    /* Dropdown menu */
    [data-baseweb="menu"],
    ul[role="listbox"] {
        background: var(--surface-white) !important;
        border: 1px solid var(--border-light) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
    }

    [data-baseweb="menu"] li,
    [role="option"],
    li[role="option"] {
        color: var(--text-dark) !important;
        background: var(--surface-white) !important;
        padding: 10px 12px !important;
    }

    [data-baseweb="menu"] li:hover,
    [role="option"]:hover,
    li[role="option"]:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%) !important;
        color: var(--primary-blue-dark) !important;
    }

    /* ========================================
       DATAFRAME / TABLES
       ======================================== */
    .dataframe,
    [data-testid="stDataFrame"],
    .stDataFrame {
        background: var(--surface-white) !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06) !important;
        overflow: hidden !important;
    }

    .dataframe thead tr th,
    [data-testid="stDataFrame"] thead tr th {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%) !important;
        color: var(--primary-blue-dark) !important;
        font-weight: 700 !important;
        padding: 14px 12px !important;
        border-bottom: 2px solid var(--primary-blue-light) !important;
    }

    .dataframe tbody tr,
    [data-testid="stDataFrame"] tbody tr {
        background: #ffffff !important;
        border-bottom: 1px solid #f0f0f0 !important;
    }

    .dataframe tbody tr td,
    [data-testid="stDataFrame"] tbody tr td {
        color: var(--text-dark) !important;
        padding: 10px 12px !important;
        background: #ffffff !important;
    }

    .dataframe tbody tr:hover,
    [data-testid="stDataFrame"] tbody tr:hover {
        background: linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%) !important;
        transform: scale(1.002) !important;
        transition: all 0.2s ease !important;
    }

    /* ========================================
       EXPANDERS
       ======================================== */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] > details > summary {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
        border: 1px solid var(--border-light) !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        font-weight: 600 !important;
    }

    .streamlit-expanderHeader:hover,
    [data-testid="stExpander"] > details > summary:hover {
        background-color: #f5f5f5 !important;
    }

    .streamlit-expanderContent,
    [data-testid="stExpander"] > details > div {
        background-color: #ffffff !important;
        border: 1px solid var(--border-light) !important;
        border-top: none !important;
        border-radius: 0 0 8px 8px !important;
        padding: 16px !important;
    }

    /* ========================================
       ALERTS / NOTIFICATIONS
       ======================================== */
    .stAlert,
    [data-testid="stNotification"],
    [data-testid="stAlert"] {
        background-color: #ffffff !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
    }

    .stAlert p, .stAlert span, .stAlert div,
    [data-testid="stNotification"] p,
    [data-testid="stAlert"] p {
        color: var(--text-dark) !important;
    }

    /* Success alerts */
    [data-testid="stAlert"][data-baseweb="notification"] div[role="alert"]:has(svg[data-testid="stSuccessIcon"]) {
        background-color: #e8f5e9 !important;
        border-left: 4px solid var(--success-green) !important;
    }

    /* Error alerts */
    [data-testid="stAlert"][data-baseweb="notification"] div[role="alert"]:has(svg[data-testid="stErrorIcon"]) {
        background-color: #ffebee !important;
        border-left: 4px solid var(--delete-red) !important;
    }

    /* Info alerts */
    [data-testid="stAlert"][data-baseweb="notification"] div[role="alert"]:has(svg[data-testid="stInfoIcon"]) {
        background-color: #e3f2fd !important;
        border-left: 4px solid var(--primary-blue) !important;
    }

    /* Warning alerts */
    [data-testid="stAlert"][data-baseweb="notification"] div[role="alert"]:has(svg[data-testid="stWarningIcon"]) {
        background-color: #fff8e1 !important;
        border-left: 4px solid #f57c00 !important;
    }

    /* ========================================
       RADIO BUTTONS
       ======================================== */
    .stRadio > label,
    [data-testid="stRadio"] label {
        color: var(--text-dark) !important;
        font-weight: 600 !important;
    }

    .stRadio div[role="radiogroup"] label,
    [data-testid="stRadio"] div[role="radiogroup"] label {
        color: var(--text-dark) !important;
        background-color: #ffffff !important;
        padding: 8px 12px !important;
        border-radius: 6px !important;
        margin: 4px !important;
    }

    .stRadio div[role="radiogroup"] label:hover {
        background-color: #f5f5f5 !important;
    }
    /* ========================================
   HORIZONTAL RADIO BUTTONS - HIGHLIGHT (WARP/WEFT Selection)
   ======================================== */
.stRadio > div[role="radiogroup"][data-testid] {
    display: flex !important;
    gap: 12px !important;
}

.stRadio > div[role="radiogroup"] > label {
    background-color: #ffffff !important;
    padding: 14px 28px !important;
    border-radius: 10px !important;
    border: 2px solid var(--border-light) !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
    flex: 1 !important;
    text-align: center !important;
    min-width: 120px !important;
}

.stRadio > div[role="radiogroup"] > label:hover {
    background-color: #e3f2fd !important;
    border: 2px solid var(--primary-blue-light) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(25, 118, 210, 0.15) !important;
}

/* Selected radio button - HIGHLIGHT */
.stRadio > div[role="radiogroup"] > label:has(input[type="radio"]:checked) {
    background: linear-gradient(135deg, var(--primary-blue) 0%, var(--accent-teal) 100%) !important;
    border: 2px solid var(--primary-blue-dark) !important;
    box-shadow: 0 6px 16px rgba(25, 118, 210, 0.3) !important;
    transform: translateY(-2px) !important;
}

.stRadio > div[role="radiogroup"] > label:has(input[type="radio"]:checked) p,
.stRadio > div[role="radiogroup"] > label:has(input[type="radio"]:checked) span,
.stRadio > div[role="radiogroup"] > label:has(input[type="radio"]:checked) div {
    color: white !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    white-space: nowrap !important;
}

/* Prevent text wrapping in all radio labels */
.stRadio > div[role="radiogroup"] > label p,
.stRadio > div[role="radiogroup"] > label span,
.stRadio > div[role="radiogroup"] > label div {
    white-space: nowrap !important;
}

/* Radio circle indicator for horizontal radios */
.stRadio div[data-baseweb="radio"] > div:first-child {
    background-color: white !important;
    border: 2px solid var(--primary-blue) !important;
}

.stRadio div[data-baseweb="radio"][data-checked="true"] > div:first-child {
    background-color: white !important;
    border: 2px solid white !important;
}

.stRadio div[data-baseweb="radio"][data-checked="true"] > div:first-child::after {
    background-color: var(--primary-blue) !important;
}

    /* ========================================
       TABS
       ======================================== */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff !important;
        border-bottom: 2px solid var(--border-light) !important;
    }

    .stTabs [data-baseweb="tab-list"] button,
    [data-testid="stTabs"] button {
        color: var(--text-dark) !important;
        background-color: #ffffff !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
    }

    .stTabs [data-baseweb="tab-list"] button:hover {
        background-color: #f5f5f5 !important;
        color: var(--primary-blue) !important;
    }

    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"],
    [data-testid="stTabs"] button[aria-selected="true"] {
        color: var(--primary-blue) !important;
        border-bottom: 3px solid var(--primary-blue) !important;
        background-color: #e3f2fd !important;
    }

    .stTabs [data-baseweb="tab-panel"] {
        background-color: #ffffff !important;
        padding: 20px !important;
        border-radius: 0 0 8px 8px !important;
    }

    /* ========================================
       FORMS
       ======================================== */
    .stForm {
        background-color: #ffffff !important;
        border: 1px solid var(--border-light) !important;
        border-radius: 10px !important;
        padding: 20px !important;
    }

    .stForm label,
    label[data-testid] {
        color: var(--text-dark) !important;
        font-weight: 600 !important;
    }

    [data-testid="stForm"] input,
    [data-testid="stForm"] textarea,
    [data-testid="stForm"] [data-baseweb="input"] {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
    }

    /* ========================================
       MARKDOWN CONTENT
       ======================================== */
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] div,
    [data-testid="stMarkdownContainer"] li {
        color: var(--text-dark) !important;
    }

    [data-testid="stMarkdownContainer"] strong {
        color: var(--primary-blue-dark) !important;
    }

    /* ========================================
       HORIZONTAL RULE
       ======================================== */
    hr {
        border: none !important;
        border-top: 2px solid var(--border-light) !important;
        margin: 24px 0 !important;
    }

    /* ========================================
       SCROLLBAR
       ======================================== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb {
        background: var(--primary-blue-light);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary-blue);
    }

    /* ========================================
       ADDITIONAL OVERRIDES
       ======================================== */
    /* Override any remaining dark mode elements */
    * {
        scrollbar-color: var(--primary-blue-light) #f1f1f1;
    }

    /* Ensure all containers are light */
    div, section, article, aside {
        background-color: transparent !important;
    }

    /* Column containers */
    [data-testid="column"] {
        background-color: transparent !important;
    }

    /* Block containers */
    [data-testid="block-container"] {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ========================================
# SIDEBAR NAVIGATION
# ========================================
st.sidebar.title("📋 Navigation Menu")
page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Dashboard",
        "📦 Add Inventory",
        "👷 Job Worker Entry",
        "✅ Finished Good Entries",
        "📊 Worker Summary",
        "💰 Caution Deposits",  # ← NEW PAGE ADDED
        "⚙️ Manage Categories"
    ],
    label_visibility="collapsed"
)

# ========================================
# DASHBOARD PAGE
# ========================================
if page == "🏠 Dashboard":
    st.markdown("<h1 class='main-header'>🏭 WARP & WEFT Management Dashboard</h1>", unsafe_allow_html=True)

    stats = st.session_state.db.get_dashboard_stats()

    if stats:
        # Row 1: Inventory Stocks
        st.subheader("📦 Inventory Stocks (Available in Warehouse)")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🧵 WARP Inventory",
                f"{stats['inventory_warp']:.2f} kg",
                "Available to distribute"
            )

        with col2:
            st.metric(
                "🎨 WEFT Inventory",
                f"{stats['inventory_weft']:.2f} kg",
                "Available to distribute"
            )

        with col3:
            total_inventory = stats['inventory_warp'] + stats['inventory_weft']
            st.metric(
                "💼 Total Available",
                f"{total_inventory:.2f} kg",
                "Ready for distribution"
            )

        st.markdown("---")

        # Row 2: Job Worker Holdings
        st.subheader("👷 Material with Job Workers")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📦 WARP Balance",
                f"{stats['job_worker_warp']:.2f} kg",
                "With job workers"
            )

        with col2:
            st.metric(
                "🧵 WEFT Balance",
                f"{stats['job_worker_weft']:.2f} kg",
                "With job workers"
            )

        with col3:
            total_jw = stats['job_worker_warp'] + stats['job_worker_weft']
            st.metric(
                "👷 Total with Workers",
                f"{total_jw:.2f} kg",
                "Distributed - Used"
            )

        st.markdown("---")

        # Row 3: Finished Products
        st.subheader("✅ Finished Products")
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "✅ Completed Products",
                f"{stats['finished_products_weight']:.2f} kg",
                f"{stats['finished_products_count']} items"
            )

        with col2:
            st.metric(
                "🎯 Total Production",
                f"{stats['total_pieces']} pieces",
                f"{stats['total_meters']:.1f} meters"
            )

        st.markdown("---")

        # ========================================
        # VIEW RECORDS SECTION (NEWLY ADDED)
        # ========================================
        st.subheader("📋 View Detailed Records")
        st.info("💡 **Tip:** Use date filters to view records for specific time periods")

        # Date Range Filter (Common for all sections)
        col1, col2 = st.columns(2)
        with col1:
            view_from_date = st.date_input(
                "View From Date",
                value=date.today() - timedelta(days=30),
                key="view_from_date"
            )
        with col2:
            view_to_date = st.date_input(
                "View To Date",
                value=date.today(),
                key="view_to_date"
            )

        if view_from_date > view_to_date:
            st.error("⚠️ From Date cannot be after To Date")
        else:
            st.markdown("---")

            # 1. INVENTORY WARP RECORDS
            with st.expander("📦 Inventory WARP Records", expanded=False):
                inventory_warp = st.session_state.db.get_inventory_warp_by_date(view_from_date, view_to_date)

                if inventory_warp:
                    df = pd.DataFrame(inventory_warp)
                    display_df = df[['warp_number', 'date', 'yarn_type', 'warper_name', 'design',
                                     'gross_weight', 'paper_weight', 'beam_weight', 'no_of_bell',
                                     'reed', 'net_weight']].copy()
                    display_df.columns = ['Warp #', 'Date', 'Yarn Type', 'Warper', 'Design',
                                          'Gross (kg)', 'Paper (kg)', 'Beam (kg)', 'Bell',
                                          'Reed', 'Net (kg)']

                    # Format reed to show "N/A" if empty
                    display_df['Reed'] = display_df['Reed'].apply(lambda x: x if x else 'N/A')

                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    # Summary
                    total_gross = df['gross_weight'].sum()
                    total_net = df['net_weight'].sum()
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.info(f"**Total Records:** {len(df)}")
                    with col2:
                        st.info(f"**Total Gross Weight:** {total_gross:.2f} kg")
                    with col3:
                        st.info(f"**Total Net Weight:** {total_net:.2f} kg")

                    # Download button
                    csv = display_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Inventory WARP (CSV)",
                        csv,
                        f"inventory_warp_{view_from_date}_{view_to_date}.csv",
                        "text/csv",
                        key='download-inv-warp'
                    )
                else:
                    st.info("No inventory WARP records found in this date range")

            # 2. INVENTORY WEFT RECORDS
            with st.expander("🧵 Inventory WEFT Records", expanded=False):
                inventory_weft = st.session_state.db.get_inventory_weft_by_date(view_from_date, view_to_date)

                if inventory_weft:
                    df = pd.DataFrame(inventory_weft)
                    display_df = df[['date', 'colour', 'gross_weight', 'no_of_cones',
                                     'cone_weight', 'no_of_bags', 'net_weight']].copy()
                    display_df.columns = ['Date', 'Colour', 'Gross (kg)', 'Cones',
                                          'Cone Wt (kg)', 'Bags', 'Net (kg)']

                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    # Summary
                    total_gross = df['gross_weight'].sum()
                    total_net = df['net_weight'].sum()
                    total_cones = df['no_of_cones'].sum()

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.info(f"**Total Records:** {len(df)}")
                    with col2:
                        st.info(f"**Total Cones:** {int(total_cones)}")
                    with col3:
                        st.info(f"**Total Gross:** {total_gross:.2f} kg")
                    with col4:
                        st.info(f"**Total Net:** {total_net:.2f} kg")

                    # Download button
                    csv = display_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Inventory WEFT (CSV)",
                        csv,
                        f"inventory_weft_{view_from_date}_{view_to_date}.csv",
                        "text/csv",
                        key='download-inv-weft'
                    )
                else:
                    st.info("No inventory WEFT records found in this date range")

            # 3. JOB WORKER WARP ENTRIES
            with st.expander("👷 Job Worker WARP Entries", expanded=False):
                jw_warp = st.session_state.db.get_job_worker_warp_with_balance(view_from_date, view_to_date)

                if jw_warp:
                    df = pd.DataFrame(jw_warp)
                    display_df = df[['warp_number', 'date', 'job_worker', 'yarn_type', 'warper_name', 'design',
                                     'gross_weight', 'paper_weight', 'beam_weight', 'no_of_bell',
                                     'reed', 'balance']].copy()
                    display_df.columns = ['Warp #', 'Date', 'Job Worker', 'Yarn Type', 'Warper', 'Design',
                                          'Gross (kg)', 'Paper (kg)', 'Beam (kg)', 'Bell',
                                          'Reed', 'Balance (kg)']

                    # Format reed to show "N/A" if empty
                    display_df['Reed'] = display_df['Reed'].apply(lambda x: x if x else 'N/A')

                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    # Summary
                    total_balance = df['balance'].iloc[-1] if len(df) > 0 else 0
                    unique_workers = df['job_worker'].nunique()

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.info(f"**Total Entries:** {len(df)}")
                    with col2:
                        st.info(f"**Unique Workers:** {unique_workers}")
                    with col3:
                        st.info(f"**Final Balance:** {total_balance:.2f} kg")

                    # Download button
                    csv = display_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Job Worker WARP (CSV)",
                        csv,
                        f"job_worker_warp_{view_from_date}_{view_to_date}.csv",
                        "text/csv",
                        key='download-jw-warp'
                    )
                else:
                    st.info("No job worker WARP entries found in this date range")

            # 4. JOB WORKER WEFT ENTRIES
            with st.expander("🎨 Job Worker WEFT Entries", expanded=False):
                jw_weft = st.session_state.db.get_job_worker_weft_with_balance(view_from_date, view_to_date)

                if jw_weft:
                    df = pd.DataFrame(jw_weft)
                    display_df = df[['date', 'job_worker', 'colour', 'gross_weight', 'no_of_cones',
                                     'cone_weight', 'no_of_bags', 'balance']].copy()
                    display_df.columns = ['Date', 'Job Worker', 'Colour', 'Gross (kg)', 'Cones',
                                          'Cone Wt (kg)', 'Bags', 'Balance (kg)']

                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    # Summary
                    total_balance = df['balance'].iloc[-1] if len(df) > 0 else 0
                    unique_workers = df['job_worker'].nunique()
                    total_cones = df['no_of_cones'].sum()

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.info(f"**Total Entries:** {len(df)}")
                    with col2:
                        st.info(f"**Unique Workers:** {unique_workers}")
                    with col3:
                        st.info(f"**Total Cones:** {int(total_cones)}")
                    with col4:
                        st.info(f"**Final Balance:** {total_balance:.2f} kg")

                    # Download button
                    csv = display_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Job Worker WEFT (CSV)",
                        csv,
                        f"job_worker_weft_{view_from_date}_{view_to_date}.csv",
                        "text/csv",
                        key='download-jw-weft'
                    )
                else:
                    st.info("No job worker WEFT entries found in this date range")

            # 5. FINISHED PRODUCTS
            with st.expander("✅ Finished Products", expanded=False):
                products = st.session_state.db.get_all_products_by_date(view_from_date, view_to_date)

                if products:
                    df = pd.DataFrame(products)
                    display_df = df[['completion_date', 'job_worker', 'product_category',
                                     'total_pieces', 'total_meters', 'product_weight',
                                     'warp_used', 'weft_used', 'notes']].copy()
                    display_df.columns = ['Date', 'Job Worker', 'Product', 'Pieces', 'Meters',
                                          'Weight (kg)', 'WARP Used (kg)', 'WEFT Used (kg)', 'Notes']

                    # Format numeric columns
                    display_df['Meters'] = display_df['Meters'].apply(lambda x: f"{x:.1f}")
                    display_df['Weight (kg)'] = display_df['Weight (kg)'].apply(lambda x: f"{x:.2f}")
                    display_df['WARP Used (kg)'] = display_df['WARP Used (kg)'].apply(lambda x: f"{x:.2f}")
                    display_df['WEFT Used (kg)'] = display_df['WEFT Used (kg)'].apply(lambda x: f"{x:.2f}")
                    display_df['Notes'] = display_df['Notes'].apply(lambda x: x if x else 'N/A')

                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    # Summary
                    total_pieces = df['total_pieces'].sum()
                    total_meters = df['total_meters'].sum()
                    total_weight = df['product_weight'].sum()
                    unique_workers = df['job_worker'].nunique()

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.info(f"**Total Products:** {len(df)}")
                    with col2:
                        st.info(f"**Total Pieces:** {int(total_pieces)}")
                    with col3:
                        st.info(f"**Total Meters:** {total_meters:.1f}m")
                    with col4:
                        st.info(f"**Total Weight:** {total_weight:.2f} kg")

                    # Download button
                    csv = display_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Finished Products (CSV)",
                        csv,
                        f"finished_products_{view_from_date}_{view_to_date}.csv",
                        "text/csv",
                        key='download-products'
                    )
                else:
                    st.info("No finished products found in this date range")



# ========================================
# ADD INVENTORY PAGE - WITH DROPDOWNS
# ========================================
elif page == "📦 Add Inventory":
    st.title("📦 Add Inventory (Procured Materials)")
    st.info("ℹ️ **Enter materials purchased from outside suppliers**")

    material_type = st.radio("Select Material Type", ["WARP", "WEFT"], horizontal=True)

    if material_type == "WARP":
        st.subheader("🧵 Add WARP to Inventory")

        # Get yarn materials, designs, warpers, and reed types from database
        yarn_materials = st.session_state.db.get_all_yarn_materials()
        design_types = st.session_state.db.get_all_design_weave_types()
        warpers = st.session_state.db.get_all_warpers()  # NEW: Task #2
        reed_types = st.session_state.db.get_all_reed_types()  # NEW: Task #7

        if not yarn_materials:
            st.warning("⚠️ Please add yarn/materials in 'Manage Categories' first")
        if not design_types:
            st.warning("⚠️ Please add design/weave types in 'Manage Categories' first")
        if not warpers:
            st.warning("⚠️ Please add warpers in 'Manage Categories' first")

        with st.form("inventory_warp_form"):
            col1, col2 = st.columns(2)

            with col1:
                entry_date = st.date_input("Date *", value=date.today())
                yarn_type = st.selectbox("Yarn/Material Type *",
                                         options=yarn_materials if yarn_materials else ["No materials available"])
                design = st.selectbox("Design/Weave Type *",
                                      options=design_types if design_types else ["No designs available"])
                warper_name = st.selectbox("Warper Name *",  # NEW: Task #2
                                           options=warpers if warpers else ["No warpers available"])

            with col2:
                gross_weight = st.number_input("Gross Weight (kg) *", min_value=0.0, step=0.01,
                                               format="%.2f")  # NEW: Task #3
                paper_weight = st.number_input("Paper Weight (kg) *", min_value=0.0, step=0.01, format="%.2f")
                beam_weight = st.number_input("Beam Weight (kg) *", min_value=0.0, step=0.01,
                                              format="%.2f")  # RENAMED: Task #5
                no_of_bell = st.number_input("No. of Bell *", min_value=0, step=1, format="%d")  # NEW: Task #6
                reed = st.selectbox("Reed (Optional)",  # NEW: Task #7
                                    options=[""] + (reed_types if reed_types else []),
                                    help="Optional field - select reed type if applicable")

            # NEW FORMULA calculation preview (Task #4)
            if gross_weight > 0:
                net_weight = gross_weight - (paper_weight + beam_weight)
                if net_weight > 0:
                    st.success(
                        f"✅ **Net Weight: {net_weight:.2f} kg** = Gross ({gross_weight:.2f} kg) - [Paper ({paper_weight:.2f} kg) + Beam ({beam_weight:.2f} kg)]")
                elif net_weight == 0:
                    st.warning("⚠️ Net weight is zero!")
                else:
                    st.error("❌ Net weight must be positive! Paper + Beam weights exceed Gross weight.")

            submitted = st.form_submit_button("💾 Save to Inventory", use_container_width=True)

            if submitted:
                if not yarn_materials or not design_types or not warpers:
                    st.error("Please add yarn/materials, designs, and warpers in 'Manage Categories' first")
                else:
                    success, messages = st.session_state.service.add_inventory_warp(
                        entry_date, yarn_type, warper_name, design, gross_weight,
                        paper_weight, beam_weight, no_of_bell, reed
                    )
                    if success:
                        for msg in messages:
                            st.success(msg)
                    else:
                        for msg in messages:
                            st.error(msg)


    else:  # WEFT

        st.subheader("🎨 Add WEFT to Inventory")

        colors = st.session_state.db.get_all_colors()

        if not colors:
            st.warning("⚠️ Please add colors in 'Manage Categories' first")

        with st.form("inventory_weft_form"):

            col1, col2 = st.columns(2)

            with col1:

                entry_date = st.date_input("Date *", value=date.today())

                colour = st.selectbox("Colour *", options=colors if colors else ["No colors available"])

                gross_weight = st.number_input("Gross Weight (kg) *", min_value=0.0, step=0.01,
                                               format="%.2f")  # NEW: Task #3

                no_of_cones = st.number_input("Number of Cones *", min_value=0, step=1, format="%d")

            with col2:

                # NEW: Task #9 - Cone Weight DROPDOWN (30g, 50g, 90g only)

                cone_weight_options = {

                    "30g (0.03 kg)": 0.03,

                    "50g (0.05 kg)": 0.05,

                    "90g (0.09 kg)": 0.09

                }

                cone_weight_label = st.selectbox("Cone Weight *", options=list(cone_weight_options.keys()))

                cone_weight = cone_weight_options[cone_weight_label]

                # NEW: Task #8 - No. of Bags (default 1, 200g per bag)

                no_of_bags = st.number_input("No. of Bags *", min_value=1, value=1, step=1, format="%d",

                                             help="Default: 1 bag (200g per bag)")

            # NEW FORMULA calculation preview (Task #4)

            BAG_WEIGHT = 0.2  # 200g per bag

            if gross_weight > 0 and no_of_cones > 0:

                net_weight = gross_weight - (cone_weight * no_of_cones + BAG_WEIGHT * no_of_bags)

                if net_weight > 0:

                    st.success(

                        f"✅ **Net Weight: {net_weight:.2f} kg** = "

                        f"Gross ({gross_weight:.2f} kg) - "

                        f"[Cones ({cone_weight * no_of_cones:.2f} kg) + Bags ({BAG_WEIGHT * no_of_bags:.2f} kg)]"

                    )

                    st.info(
                        f"📊 Breakdown: {no_of_cones} cones × {cone_weight}kg + {no_of_bags} bags × 0.2kg = {cone_weight * no_of_cones + BAG_WEIGHT * no_of_bags:.2f} kg total deduction")

                elif net_weight == 0:

                    st.warning("⚠️ Net weight is zero!")

                else:

                    st.error("❌ Net weight must be positive! Cone + Bag weights exceed Gross weight.")

            submitted = st.form_submit_button("💾 Save to Inventory", use_container_width=True)

            if submitted:

                if not colors:

                    st.error("Please add colors first")

                elif gross_weight == 0:

                    st.error("Gross weight must be greater than 0")

                elif no_of_cones == 0:

                    st.error("Number of cones must be greater than 0")

                else:

                    success, messages = st.session_state.service.add_inventory_weft(

                        entry_date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags

                    )

                    if success:

                        for msg in messages:
                            st.success(msg)

                    else:

                        for msg in messages:
                            st.error(msg)

# ========================================
# JOB WORKER ENTRY PAGE - WITH DROPDOWNS
# ========================================
elif page == "👷 Job Worker Entry":
    st.title("👷 Job Worker Entry (Material Distribution)")
    st.info("ℹ️ **Distribute materials to job workers from inventory**")

    workers = st.session_state.db.get_all_job_workers()

    if not workers:
        st.warning("⚠️ Please add job workers in 'Manage Categories' first")

    # Show available inventory
    available_warp = st.session_state.db.get_available_inventory_warp()
    available_weft = st.session_state.db.get_available_inventory_weft()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("📦 Available WARP Inventory", f"{available_warp:.2f} kg")
    with col2:
        st.metric("🧵 Available WEFT Inventory", f"{available_weft:.2f} kg")

    st.markdown("---")

    material_type = st.radio("Select Material Type", ["WARP", "WEFT"], horizontal=True)

    if material_type == "WARP":
        st.subheader("📦 Distribute WARP to Job Worker")

        # Get yarn materials, designs, warpers, and reed types from database
        yarn_materials = st.session_state.db.get_all_yarn_materials()
        design_types = st.session_state.db.get_all_design_weave_types()
        warpers = st.session_state.db.get_all_warpers()  # NEW: Task #2
        reed_types = st.session_state.db.get_all_reed_types()  # NEW: Task #7

        if not yarn_materials:
            st.warning("⚠️ Please add yarn/materials in 'Manage Categories' first")
        if not design_types:
            st.warning("⚠️ Please add design/weave types in 'Manage Categories' first")
        if not warpers:
            st.warning("⚠️ Please add warpers in 'Manage Categories' first")

        with st.form("job_worker_warp_form"):
            col1, col2 = st.columns(2)

            with col1:
                entry_date = st.date_input("Date *", value=date.today())
                yarn_type = st.selectbox("Yarn/Material Type *",
                                         options=yarn_materials if yarn_materials else ["No materials available"])
                design = st.selectbox("Design/Weave Type *",
                                      options=design_types if design_types else ["No designs available"])
                warper_name = st.selectbox("Warper Name *",  # NEW: Task #2
                                           options=warpers if warpers else ["No warpers available"])
                job_worker = st.selectbox("Job Worker *", options=workers if workers else ["No workers available"])

            with col2:
                gross_weight = st.number_input("Gross Weight (kg) *", min_value=0.0, step=0.01,
                                               format="%.2f")  # NEW: Task #3
                paper_weight = st.number_input("Paper Weight (kg) *", min_value=0.0, step=0.01, format="%.2f")
                beam_weight = st.number_input("Beam Weight (kg) *", min_value=0.0, step=0.01,
                                              format="%.2f")  # RENAMED: Task #5
                no_of_bell = st.number_input("No. of Bell *", min_value=0, step=1, format="%d")  # NEW: Task #6
                reed = st.selectbox("Reed (Optional)",  # NEW: Task #7
                                    options=[""] + (reed_types if reed_types else []),
                                    help="Optional field - select reed type if applicable")

            # NEW FORMULA calculation preview (Task #4)
            if gross_weight > 0:
                net_weight = gross_weight - (paper_weight + beam_weight)
                if net_weight > 0:
                    if net_weight > available_warp:
                        st.error(
                            f"❌ Insufficient inventory! Required: {net_weight:.2f} kg, Available: {available_warp:.2f} kg")
                    else:
                        st.success(f"✅ **Net Weight: {net_weight:.2f} kg** will be distributed to {job_worker}")
                        st.info(
                            f"📊 Calculation: Gross ({gross_weight:.2f} kg) - [Paper ({paper_weight:.2f} kg) + Beam ({beam_weight:.2f} kg)]")
                        st.info(f"📦 Remaining inventory after distribution: {available_warp - net_weight:.2f} kg")
                elif net_weight == 0:
                    st.warning("⚠️ Net weight is zero!")
                else:
                    st.error("❌ Net weight must be positive! Paper + Beam weights exceed Gross weight.")

            submitted = st.form_submit_button("👷 Distribute to Worker", use_container_width=True)

            if submitted:
                if not yarn_materials or not design_types or not warpers or not workers:
                    st.error(
                        "Please fill in all required fields and ensure workers, materials, designs, and warpers exist")
                else:
                    success, messages = st.session_state.service.add_job_worker_warp(
                        entry_date, yarn_type, warper_name, design, gross_weight,
                        paper_weight, beam_weight, no_of_bell, reed, job_worker
                    )
                    if success:
                        for msg in messages:
                            st.success(msg)
                    else:
                        for msg in messages:
                            st.error(msg)


    else:  # WEFT

        st.subheader("🧵 Distribute WEFT to Job Worker")

        colors = st.session_state.db.get_all_colors()

        if not colors or not workers:
            st.warning("⚠️ Please add colors and job workers in 'Manage Categories' first")

        with st.form("job_worker_weft_form"):

            col1, col2 = st.columns(2)

            with col1:

                entry_date = st.date_input("Date *", value=date.today())

                colour = st.selectbox("Colour *", options=colors if colors else ["No colors available"])

                gross_weight = st.number_input("Gross Weight (kg) *", min_value=0.0, step=0.01,
                                               format="%.2f")  # NEW: Task #3

                no_of_cones = st.number_input("Number of Cones *", min_value=0, step=1, format="%d")

                job_worker = st.selectbox("Job Worker *", options=workers if workers else ["No workers available"])

            with col2:

                # NEW: Task #9 - Cone Weight DROPDOWN (30g, 50g, 90g only)

                cone_weight_options = {

                    "30g (0.03 kg)": 0.03,

                    "50g (0.05 kg)": 0.05,

                    "90g (0.09 kg)": 0.09

                }

                cone_weight_label = st.selectbox("Cone Weight *", options=list(cone_weight_options.keys()))

                cone_weight = cone_weight_options[cone_weight_label]

                # NEW: Task #8 - No. of Bags (default 1, 200g per bag)

                no_of_bags = st.number_input("No. of Bags *", min_value=1, value=1, step=1, format="%d",

                                             help="Default: 1 bag (200g per bag)")

            # NEW FORMULA calculation preview (Task #4)

            BAG_WEIGHT = 0.2  # 200g per bag

            if gross_weight > 0 and no_of_cones > 0:

                net_weight = gross_weight - (cone_weight * no_of_cones + BAG_WEIGHT * no_of_bags)

                if net_weight > 0:

                    if net_weight > available_weft:

                        st.error(
                            f"❌ Insufficient inventory! Required: {net_weight:.2f} kg, Available: {available_weft:.2f} kg")

                    else:

                        st.success(f"✅ **Net Weight: {net_weight:.2f} kg** will be distributed to {job_worker}")

                        st.info(

                            f"📊 Calculation: Gross ({gross_weight:.2f} kg) - "

                            f"[Cones ({cone_weight * no_of_cones:.2f} kg) + Bags ({BAG_WEIGHT * no_of_bags:.2f} kg)]"

                        )

                        st.info(f"📦 Remaining inventory after distribution: {available_weft - net_weight:.2f} kg")

                elif net_weight == 0:

                    st.warning("⚠️ Net weight is zero!")

                else:

                    st.error("❌ Net weight must be positive! Cone + Bag weights exceed Gross weight.")

            submitted = st.form_submit_button("👷 Distribute to Worker", use_container_width=True)

            if submitted:

                if not colors or not workers:

                    st.error("Please add colors and workers first")

                elif gross_weight == 0:

                    st.error("Gross weight must be greater than 0")

                elif no_of_cones == 0:

                    st.error("Number of cones must be greater than 0")

                else:

                    success, messages = st.session_state.service.add_job_worker_weft(

                        entry_date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags, job_worker

                    )

                    if success:

                        for msg in messages:
                            st.success(msg)

                    else:

                        for msg in messages:
                            st.error(msg)

# ========================================
# COMPLETE PRODUCT PAGE
# ========================================
elif page == "✅ Finished Good Entries":
    st.title("✅ Finished Good Entries")

    workers = st.session_state.db.get_all_job_workers()
    categories = st.session_state.db.get_all_product_categories()

    if not workers or not categories:
        st.warning("⚠️ Please add job workers and product categories in 'Manage Categories' first")

    st.markdown("### 👷 Select Job Worker")
    selected_worker = st.selectbox(
        "Job Worker *",
        options=workers if workers else ["No workers available"],
        key="worker_select"
    )

    # Show worker details
    if selected_worker and selected_worker != "No workers available":
        worker_details = st.session_state.db.get_job_worker_details(selected_worker)

        if worker_details:
            st.markdown("### 📋 Worker Information")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.info(f"**Name:**\n{worker_details['worker_name']}")
            with col2:
                contact = worker_details['contact_number'] if worker_details['contact_number'] else "N/A"
                st.info(f"**Contact:**\n{contact}")
            with col3:
                gst = worker_details['gst_number'] if worker_details['gst_number'] else "N/A"
                st.info(f"**GST:**\n{gst}")
            with col4:
                aadhar = worker_details['aadhar_number'] if worker_details['aadhar_number'] else "N/A"
                st.info(f"**Aadhar:**\n{aadhar}")

        # Show available balance
        balance = st.session_state.db.get_worker_balance(selected_worker)

        if balance:
            st.markdown("### 💼 Available Material Balance")
            col1, col2, col3 = st.columns(3)

            # with col1:
            #     st.metric("📦 WARP Balance", f"{balance['warp_balance']:.2f} kg")
            # with col2:
            #     st.metric("🧵 WEFT Balance", f"{balance['weft_balance']:.2f} kg")
            with col1:
                total_balance = balance['warp_balance'] + balance['weft_balance']
                st.metric("💼 Total Balance", f"{total_balance:.2f} kg")

    st.markdown("---")

    # Product completion form
    with st.form("product_form"):
        col1, col2 = st.columns(2)

        with col1:
            product_category = st.selectbox(
                "Product Category *",
                options=categories if categories else ["No categories available"]
            )
            completion_date = st.date_input("Completion Date *", value=date.today())
            total_pieces = st.number_input("Total Pieces *", min_value=1, step=1, format="%d")

        with col2:
            total_meters = st.number_input("Total Meters *", min_value=0.1, step=0.1, format="%.1f")
            product_weight = st.number_input("Product Weight (kg) *", min_value=0.0, step=0.01, format="%.2f")
            notes = st.text_area("Notes (Optional)", placeholder="Any additional information...")

        if product_weight > 0:
            warp_used = product_weight / 2
            weft_used = product_weight / 2

            st.markdown("### 📊 Material Usage (Auto-Divided Equally)")
            col1, col2 = st.columns(2)

            with col1:
                st.info(
                    f"**WARP Used:** {warp_used:.2f} kg\n\n**WEFT Used:** {weft_used:.2f} kg\n\n**Total:** {product_weight:.2f} kg")

            with col2:
                if selected_worker and selected_worker != "No workers available" and balance:
                    remaining_warp = balance['warp_balance'] - warp_used
                    remaining_weft = balance['weft_balance'] - weft_used
                    total_remaining = remaining_warp + remaining_weft

                    if remaining_warp < 0 or remaining_weft < 0:
                        st.error(
                            f"⚠️ **Insufficient Balance!**\n\nWARP: {remaining_warp:.2f} kg\nWEFT: {remaining_weft:.2f} kg")
                    else:
                        st.success(
                            f"**Remaining Balance:**\n\nWARP: {remaining_warp:.2f} kg\nWEFT: {remaining_weft:.2f} kg\nTotal: {total_remaining:.2f} kg")

        submitted = st.form_submit_button("✅ Complete Product", use_container_width=True)

        if submitted:
            if not workers or not categories or selected_worker == "No workers available":
                st.error("Please ensure job workers and product categories are added")
            elif not product_category or product_category == "No categories available":
                st.error("Please select a valid product category")
            else:
                success, messages = st.session_state.service.complete_product(
                    selected_worker, product_category, completion_date,
                    total_pieces, total_meters, product_weight, notes
                )

                if success:
                    for msg in messages:
                        st.success(msg)
                    st.balloons()
                    # FORCE REFRESH - Added this line
                    st.rerun()
                else:
                    for msg in messages:
                        st.error(msg)

# ========================================
# WORKER SUMMARY PAGE
# ========================================
elif page == "📊 Worker Summary":
    st.title("📊 Job Worker Summary")

    workers = st.session_state.db.get_all_job_workers()

    if not workers:
        st.warning("⚠️ No job workers found. Please add workers in 'Manage Categories'")
    else:
        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            selected_worker = st.selectbox("Select Job Worker", options=workers)

        with col2:
            from_date = st.date_input("From Date", value=date.today() - timedelta(days=365))

        with col3:
            to_date = st.date_input("To Date", value=date.today())

        if from_date > to_date:
            st.error("❌ From Date cannot be after To Date")
        else:
            if selected_worker:
                worker_details = st.session_state.db.get_job_worker_details(selected_worker)

                if worker_details:
                    st.markdown(f"### 📋 Summary for: **{selected_worker}**")
                    st.markdown(f"**Period:** {from_date.strftime('%d %b %Y')} to {to_date.strftime('%d %b %Y')}")

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.info(
                            f"**Contact:**\n{worker_details['contact_number'] if worker_details['contact_number'] else 'N/A'}")
                    with col2:
                        st.info(f"**GST:**\n{worker_details['gst_number'] if worker_details['gst_number'] else 'N/A'}")
                    with col3:
                        st.info(
                            f"**Aadhar:**\n{worker_details['aadhar_number'] if worker_details['aadhar_number'] else 'N/A'}")
                        with col4:
                            balance = st.session_state.db.get_worker_balance(selected_worker)
                            if balance:
                                total = balance['warp_balance'] + balance['weft_balance']
                                st.info(f"**Current Balance:**\n{total:.2f} kg")

                    # ADD THIS NEW SECTION HERE ↓
                    st.markdown("---")
                    st.markdown("### 💼 Total Material Balance")

                    # Get summary with balance
                    summary_data = st.session_state.db.get_worker_summary_with_balance(
                        selected_worker, from_date, to_date
                    )

                    if summary_data:
                        col1, col2, col3, col4, col5 = st.columns(5)

                        with col1:
                            st.metric(
                                "WARP Distributed",
                                f"{summary_data['warp_distributed']:.2f} kg",
                                help="Total WARP given to worker in this period"
                            )

                        with col2:
                            st.metric(
                                "WEFT Distributed",
                                f"{summary_data['weft_distributed']:.2f} kg",
                                help="Total WEFT given to worker in this period"
                            )

                        with col3:
                            st.metric(
                                "Material Used",
                                f"{summary_data['material_used']:.2f} kg",
                                help="Total material used in products"
                            )

                        with col4:
                            st.metric(
                                "Period Balance",
                                f"{summary_data['balance']:.2f} kg",
                                help="Remaining balance for this period"
                            )

                        with col5:
                            current_balance = st.session_state.db.get_worker_balance(selected_worker)
                            total_current = (current_balance['warp_balance'] +
                                             current_balance['weft_balance']) if current_balance else 0
                            st.metric(
                                "Current Total Balance",
                                f"{total_current:.2f} kg",
                                help="Current balance across all time"
                            )

                    st.markdown("---")  # EXISTING LINE - keep this

                    # WARP Entries section continues below...
                    st.markdown("### 📦 WARP Entries")

                st.markdown("---")




                # WARP Entries
                st.markdown("### 📦 WARP Entries")
                warp_data = st.session_state.db.get_job_worker_warp_by_date(selected_worker, from_date, to_date)

                if warp_data:
                    df = pd.DataFrame(warp_data)
                    display_df = df[['warp_number', 'date', 'yarn_type', 'warper_name', 'design',
                                     'gross_weight', 'paper_weight', 'beam_weight', 'no_of_bell',
                                     'reed', 'net_weight']].copy()
                    display_df.columns = ['Warp #', 'Date', 'Yarn Type', 'Warper', 'Design',
                                          'Gross (kg)', 'Paper (kg)', 'Beam (kg)', 'Bell',
                                          'Reed', 'Net (kg)']
                    # Format reed to show "N/A" if empty
                    display_df['Reed'] = display_df['Reed'].apply(lambda x: x if x else 'N/A')
                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    total_warp = df['net_weight'].sum()
                    st.info(f"**Total WARP in period: {total_warp:.2f} kg** ({len(df)} entries)")
                else:
                    st.info("No WARP entries in this period")

                st.markdown("---")

                # WEFT Entries
                st.markdown("### 🧵 WEFT Entries")
                weft_data = st.session_state.db.get_job_worker_weft_by_date(selected_worker, from_date, to_date)

                if weft_data:
                    df = pd.DataFrame(weft_data)
                    display_df = df[['date', 'colour', 'gross_weight', 'no_of_cones',
                                     'cone_weight', 'no_of_bags', 'net_weight']].copy()
                    display_df.columns = ['Date', 'Colour', 'Gross (kg)', 'Cones',
                                          'Cone Wt (kg)', 'Bags', 'Net (kg)']
                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    total_weft = df['net_weight'].sum()
                    st.info(f"**Total WEFT in period: {total_weft:.2f} kg** ({len(df)} entries)")
                else:
                    st.info("No WEFT entries in this period")

                st.markdown("---")

                # Completed Products
                st.markdown("### ✅ Completed Products")
                products = st.session_state.db.get_products_by_worker_and_date(selected_worker, from_date, to_date)

                if products:
                    df = pd.DataFrame(products)
                    display_df = df[['completion_date', 'product_category', 'total_pieces', 'total_meters',
                                     'product_weight', 'warp_used', 'weft_used']].copy()

                    display_df.columns = ['Date', 'Product', 'Pieces', 'Meters', 'Weight (kg)', 'WARP Used (kg)',
                                          'WEFT Used (kg)']

                    display_df['Meters'] = display_df['Meters'].apply(lambda x: f"{x:.1f}")
                    display_df['Weight (kg)'] = display_df['Weight (kg)'].apply(lambda x: f"{x:.2f}")
                    display_df['WARP Used (kg)'] = display_df['WARP Used (kg)'].apply(lambda x: f"{x:.2f}")
                    display_df['WEFT Used (kg)'] = display_df['WEFT Used (kg)'].apply(lambda x: f"{x:.2f}")

                    st.dataframe(display_df, use_container_width=True, hide_index=True)

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.info(f"**Products:** {len(df)}")
                    with col2:
                        total_pieces_sum = df['total_pieces'].sum()
                        st.info(f"**Total Pieces:** {total_pieces_sum}")
                    with col3:
                        total_weight = df['product_weight'].sum()
                        st.info(f"**Total Weight:** {total_weight:.2f} kg")
                    with col4:
                        total_warp_used = df['warp_used'].sum()
                        total_weft_used = df['weft_used'].sum()
                        st.info(f"**Material Used:** {total_warp_used + total_weft_used:.2f} kg")
                else:
                    st.info("No completed products in this period")

                # Download button
                if warp_data or weft_data or products:
                    st.markdown("---")
                    st.markdown("### 📥 Export Data")

                    report_data = []

                    if warp_data:
                        for item in warp_data:
                            report_data.append({
                                'Type': 'WARP Entry',
                                'Date': item['date'],
                                'Details': f"{item['yarn_type']} - {item['design']}",  # FIXED: yarn_name → yarn_type
                                'Quantity': f"{item['net_weight']:.2f} kg",
                                'Job Worker': selected_worker
                            })

                    if weft_data:
                        for item in weft_data:
                            report_data.append({
                                'Type': 'WEFT Entry',
                                'Date': item['date'],
                                'Details': f"{item['colour']} - {item['no_of_cones']} cones",
                                'Quantity': f"{item['net_weight']:.2f} kg",  # FIXED: total_weight → net_weight
                                'Job Worker': selected_worker
                            })

                    if products:
                        for item in products:
                            report_data.append({
                                'Type': 'Completed Product',
                                'Date': item['completion_date'],
                                'Details': f"{item['product_category']} - {item['total_pieces']} pcs",
                                'Quantity': f"{item['product_weight']:.2f} kg",
                                'Job Worker': selected_worker
                            })

                    if report_data:
                        report_df = pd.DataFrame(report_data)
                        csv = report_df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            "📥 Download Worker Summary (CSV)",
                            csv,
                            f"worker_summary_{selected_worker}_{from_date}_{to_date}.csv",
                            "text/csv",
                            key='download-worker-summary'
                        )



# ========================================
# CAUTION DEPOSIT TRACKING PAGE (NEW)
# ========================================
elif page == "💰 Caution Deposits":
    st.title("💰 Caution Deposit Tracking")

    # Tab selection
    tab1, tab2, tab3 = st.tabs([
        "📄 Paper Deposits (WARP)",
        "📦 Bag Deposits (WEFT)",
        "📊 Summary Report"
    ])

    # ========================================
    # TAB 1: PAPER DEPOSITS (WARP)
    # ========================================
    with tab1:
        st.subheader("📄 Paper Caution Deposits - ₹40/kg")

        # Get all job workers for filter
        workers = st.session_state.db.get_all_job_workers()

        col1, col2 = st.columns([3, 1])

        with col1:
            selected_worker_filter = st.selectbox(
                "Filter by Job Worker (Optional)",
                options=["All Workers"] + workers if workers else ["All Workers"]
            )

        with col2:
            st.metric("Deposit Rate", "₹40 per kg", "Paper weight")

        # Get pending deposits
        if selected_worker_filter == "All Workers":
            pending_deposits = st.session_state.db.get_pending_paper_deposits()
        else:
            pending_deposits = st.session_state.db.get_pending_paper_deposits(selected_worker_filter)

        if pending_deposits:
            st.markdown("---")
            st.markdown("### 📋 Pending Paper Deposits")

            for idx, deposit in enumerate(pending_deposits):
                with st.expander(
                        f"🔸 Warp #{deposit['warp_number']} - {deposit['job_worker']} - "
                        f"₹{deposit['caution_deposit_paper']:.2f}",
                        expanded=False
                ):
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.info(f"**Date:** {deposit['date']}")
                        st.info(f"**Paper Weight:** {deposit['paper_weight']:.2f} kg")
                        st.info(f"**Deposit Amount:** ₹{deposit['caution_deposit_paper']:.2f}")

                    with col2:
                        paper_status = "✅ Returned" if deposit['paper_returned'] else "⏳ Pending"
                        st.info(f"**Paper Status:** {paper_status}")

                        if deposit['paper_returned']:
                            st.info(f"**Return Date:** {deposit['paper_return_date']}")

                        refund_status = "✅ Refunded" if deposit['deposit_refunded'] else "❌ Not Refunded"
                        st.info(f"**Refund Status:** {refund_status}")

                    with col3:
                        st.markdown("#### 🔧 Actions")

                        # Mark Paper Returned
                        if not deposit['paper_returned']:
                            with st.form(f"return_paper_{deposit['id']}"):
                                return_date = st.date_input(
                                    "Paper Return Date",
                                    value=date.today(),
                                    key=f"paper_return_date_{deposit['id']}"
                                )

                                if st.form_submit_button("📄 Mark Paper Returned", use_container_width=True):
                                    success, messages = st.session_state.service.mark_paper_return(
                                        deposit['id'], return_date
                                    )
                                    if success:
                                        for msg in messages:
                                            st.success(msg)
                                        st.rerun()
                                    else:
                                        for msg in messages:
                                            st.error(msg)

                        # Process Refund
                        if deposit['paper_returned'] and not deposit['deposit_refunded']:
                            with st.form(f"refund_paper_{deposit['id']}"):
                                refund_date = st.date_input(
                                    "Refund Date",
                                    value=date.today(),
                                    key=f"paper_refund_date_{deposit['id']}"
                                )

                                if st.form_submit_button("💰 Process Refund", use_container_width=True):
                                    success, messages = st.session_state.service.process_paper_deposit_refund(
                                        deposit['id'], refund_date
                                    )
                                    if success:
                                        for msg in messages:
                                            st.success(msg)
                                        st.balloons()
                                        st.rerun()
                                    else:
                                        for msg in messages:
                                            st.error(msg)

                        if deposit['deposit_refunded']:
                            st.success(f"✅ Refunded on {deposit['deposit_refund_date']}")

            # Summary
            total_pending = sum([d['caution_deposit_paper'] for d in pending_deposits if not d['deposit_refunded']])
            total_paper_pending = sum([d['paper_weight'] for d in pending_deposits if not d['paper_returned']])

            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Pending Deposits", f"₹{total_pending:.2f}")
            with col2:
                st.metric("Papers Not Returned", f"{total_paper_pending:.2f} kg")
            with col3:
                st.metric("Total Records", len(pending_deposits))
        else:
            st.info("✅ No pending paper deposits found!")

    # ========================================
    # TAB 2: BAG DEPOSITS (WEFT)
    # ========================================
    with tab2:
        st.subheader("📦 Bag Caution Deposits - ₹15/bag")

        col1, col2 = st.columns([3, 1])

        with col1:
            selected_worker_filter_bag = st.selectbox(
                "Filter by Job Worker (Optional)",
                options=["All Workers"] + workers if workers else ["All Workers"],
                key="bag_worker_filter"
            )

        with col2:
            st.metric("Deposit Rate", "₹15 per bag", "Fixed rate")

        # Get pending bag deposits
        if selected_worker_filter_bag == "All Workers":
            pending_bag_deposits = st.session_state.db.get_pending_bag_deposits()
        else:
            pending_bag_deposits = st.session_state.db.get_pending_bag_deposits(selected_worker_filter_bag)

        if pending_bag_deposits:
            st.markdown("---")
            st.markdown("### 📋 Pending Bag Deposits")

            for idx, deposit in enumerate(pending_bag_deposits):
                bags_remaining = deposit['no_of_bags'] - (deposit['bags_returned'] or 0)

                with st.expander(
                        f"🔸 {deposit['job_worker']} - {deposit['colour']} - "
                        f"₹{deposit['caution_deposit_bags']:.2f} ({bags_remaining} bags pending)",
                        expanded=False
                ):
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.info(f"**Date:** {deposit['date']}")
                        st.info(f"**Colour:** {deposit['colour']}")
                        st.info(f"**Total Bags Issued:** {deposit['no_of_bags']}")
                        st.info(f"**Deposit Amount:** ₹{deposit['caution_deposit_bags']:.2f}")

                    with col2:
                        bags_returned = deposit['bags_returned'] or 0
                        st.info(f"**Bags Returned:** {bags_returned}/{deposit['no_of_bags']}")

                        if deposit['bag_return_date']:
                            st.info(f"**Last Return Date:** {deposit['bag_return_date']}")

                        refund_status = "✅ Refunded" if deposit['deposit_refunded'] else "❌ Not Refunded"
                        st.info(f"**Refund Status:** {refund_status}")

                        if bags_remaining > 0:
                            st.warning(f"⚠️ {bags_remaining} bags still pending")
                        else:
                            st.success("✅ All bags returned!")

                    with col3:
                        st.markdown("#### 🔧 Actions")

                        # Mark Bags Returned (Partial/Full)
                        if bags_remaining > 0:
                            with st.form(f"return_bags_{deposit['id']}"):
                                bags_to_return = st.number_input(
                                    "Bags Being Returned",
                                    min_value=1,
                                    max_value=bags_remaining,
                                    value=min(1, bags_remaining),
                                    step=1,
                                    key=f"bags_return_count_{deposit['id']}"
                                )

                                return_date = st.date_input(
                                    "Bag Return Date",
                                    value=date.today(),
                                    key=f"bag_return_date_{deposit['id']}"
                                )

                                if st.form_submit_button("📦 Mark Bags Returned", use_container_width=True):
                                    total_returned = bags_returned + bags_to_return
                                    success, messages = st.session_state.service.mark_bag_return(
                                        deposit['id'], total_returned, return_date
                                    )
                                    if success:
                                        for msg in messages:
                                            st.success(msg)
                                        st.rerun()
                                    else:
                                        for msg in messages:
                                            st.error(msg)

                        # Process Refund (only if all bags returned)
                        if bags_remaining == 0 and not deposit['deposit_refunded']:
                            with st.form(f"refund_bags_{deposit['id']}"):
                                refund_date = st.date_input(
                                    "Refund Date",
                                    value=date.today(),
                                    key=f"bag_refund_date_{deposit['id']}"
                                )

                                if st.form_submit_button("💰 Process Refund", use_container_width=True):
                                    success, messages = st.session_state.service.process_bag_deposit_refund(
                                        deposit['id'], refund_date
                                    )
                                    if success:
                                        for msg in messages:
                                            st.success(msg)
                                        st.balloons()
                                        st.rerun()
                                    else:
                                        for msg in messages:
                                            st.error(msg)

                        if deposit['deposit_refunded']:
                            st.success(f"✅ Refunded on {deposit['deposit_refund_date']}")

            # Summary
            total_pending_bag = sum(
                [d['caution_deposit_bags'] for d in pending_bag_deposits if not d['deposit_refunded']])
            total_bags_not_returned = sum([
                d['no_of_bags'] - (d['bags_returned'] or 0)
                for d in pending_bag_deposits
            ])

            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Pending Deposits", f"₹{total_pending_bag:.2f}")
            with col2:
                st.metric("Bags Not Returned", total_bags_not_returned)
            with col3:
                st.metric("Total Records", len(pending_bag_deposits))
        else:
            st.info("✅ No pending bag deposits found!")

    # ========================================
    # TAB 3: SUMMARY REPORT
    # ========================================
    with tab3:
        st.subheader("📊 Caution Deposit Summary Report")

        workers = st.session_state.db.get_all_job_workers()

        if workers:
            st.markdown("### 👷 Worker-wise Deposit Summary")

            summary_data = []

            for worker in workers:
                deposits = st.session_state.db.get_total_pending_deposits_by_worker(worker)

                if deposits['total_pending'] > 0:
                    summary_data.append({
                        'Job Worker': worker,
                        'Paper Deposits (₹)': f"₹{deposits['paper_deposits']:.2f}",
                        'Bag Deposits (₹)': f"₹{deposits['bag_deposits']:.2f}",
                        'Total Pending (₹)': f"₹{deposits['total_pending']:.2f}"
                    })

            if summary_data:
                df = pd.DataFrame(summary_data)
                st.dataframe(df, use_container_width=True, hide_index=True)

                # Overall totals
                total_paper = sum(
                    [st.session_state.db.get_total_pending_deposits_by_worker(w)['paper_deposits'] for w in workers])
                total_bag = sum(
                    [st.session_state.db.get_total_pending_deposits_by_worker(w)['bag_deposits'] for w in workers])
                total_all = total_paper + total_bag

                st.markdown("---")
                st.markdown("### 💰 Overall Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Total Paper Deposits", f"₹{total_paper:.2f}")
                with col2:
                    st.metric("Total Bag Deposits", f"₹{total_bag:.2f}")
                with col3:
                    st.metric("Grand Total Pending", f"₹{total_all:.2f}")
                with col4:
                    st.metric("Workers with Deposits", len(summary_data))

                # Download report
                st.markdown("---")
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "📥 Download Summary Report (CSV)",
                    csv,
                    f"caution_deposit_summary_{date.today()}.csv",
                    "text/csv",
                    key='download-deposit-summary'
                )
            else:
                st.success("✅ No pending deposits found for any worker!")
        else:
            st.info("No job workers found. Please add workers first.")


# ========================================
# MANAGE CATEGORIES PAGE - WITH 5 TABS
# ========================================
elif page == "⚙️ Manage Categories":
    st.title("⚙️ Manage Categories")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🎨 Colors",
        "🧵 Yarn/Materials",
        "🎭 Design/Weave Types",
        "👷 Warpers",  # NEW: Task #2
        "🔧 Reed Types",  # NEW: Task #7
        "👨‍🏭 Job Workers",
        "📦 Product Categories"
    ])

    # TAB 1: COLORS
    with tab1:
        st.subheader("🎨 Color Management")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("#### Current Colors")
            colors = st.session_state.db.get_all_colors()

            if colors:
                for idx, color in enumerate(colors):
                    col_a, col_b, col_c = st.columns([3, 1, 1])

                    with col_a:
                        st.write(f"**{idx + 1}.** {color}")

                    with col_b:
                        if st.button("✏️ Edit", key=f"edit_color_{idx}", help=f"Edit {color}"):
                            st.session_state[f'editing_color_{idx}'] = True

                    with col_c:
                        if st.button("🗑️ Delete", key=f"del_color_{idx}", help=f"Delete {color}"):
                            usage_count = st.session_state.db.check_color_usage(color)
                            if usage_count > 0:
                                st.warning(f"⚠️ Cannot delete! '{color}' is used in {usage_count} records")
                            else:
                                if st.session_state.db.delete_color(color):
                                    st.success(f"Deleted: {color}")
                                    st.rerun()

                    if st.session_state.get(f'editing_color_{idx}', False):
                        with st.form(f"edit_form_color_{idx}"):
                            new_name = st.text_input("New Color Name", value=color)
                            col_save, col_cancel = st.columns(2)

                            with col_save:
                                if st.form_submit_button("💾 Save"):
                                    if st.session_state.db.update_color(color, new_name):
                                        st.success(f"Updated to: {new_name}")
                                        st.session_state[f'editing_color_{idx}'] = False
                                        st.rerun()

                            with col_cancel:
                                if st.form_submit_button("❌ Cancel"):
                                    st.session_state[f'editing_color_{idx}'] = False
                                    st.rerun()
            else:
                st.info("No colors available")

        with col2:
            st.markdown("#### Add New Color")
            with st.form("add_color_form"):
                new_color = st.text_input("Color Name")
                submitted = st.form_submit_button("➕ Add", use_container_width=True)

                if submitted:
                    if new_color:
                        success, messages = st.session_state.service.add_color(new_color)
                        if success:
                            for msg in messages:
                                st.success(msg)
                            st.rerun()
                        else:
                            for msg in messages:
                                st.error(msg)
                    else:
                        st.error("Please enter a color name")

    # TAB 2: YARN/MATERIALS (NEW)
    with tab2:
        st.subheader("🧵 Yarn/Material Management")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("#### Current Yarn/Materials")
            materials = st.session_state.db.get_all_yarn_materials()

            if materials:
                for idx, material in enumerate(materials):
                    col_a, col_b, col_c = st.columns([3, 1, 1])

                    with col_a:
                        st.write(f"**{idx + 1}.** {material}")

                    with col_b:
                        if st.button("✏️ Edit", key=f"edit_material_{idx}", help=f"Edit {material}"):
                            st.session_state[f'editing_material_{idx}'] = True

                    with col_c:
                        if st.button("🗑️ Delete", key=f"del_material_{idx}", help=f"Delete {material}"):
                            usage_count = st.session_state.db.check_yarn_material_usage(material)
                            if usage_count > 0:
                                st.warning(f"⚠️ Cannot delete! '{material}' is used in {usage_count} records")
                            else:
                                if st.session_state.db.delete_yarn_material(material):
                                    st.success(f"Deleted: {material}")
                                    st.rerun()

                    if st.session_state.get(f'editing_material_{idx}', False):
                        with st.form(f"edit_form_material_{idx}"):
                            new_name = st.text_input("New Material Name", value=material)
                            col_save, col_cancel = st.columns(2)

                            with col_save:
                                if st.form_submit_button("💾 Save"):
                                    if st.session_state.db.update_yarn_material(material, new_name):
                                        st.success(f"Updated to: {new_name}")
                                        st.session_state[f'editing_material_{idx}'] = False
                                        st.rerun()

                            with col_cancel:
                                if st.form_submit_button("❌ Cancel"):
                                    st.session_state[f'editing_material_{idx}'] = False
                                    st.rerun()
            else:
                st.info("No yarn/materials available")

        with col2:
            st.markdown("#### Add New Material")
            with st.form("add_material_form"):
                new_material = st.text_input("Material Name")
                submitted = st.form_submit_button("➕ Add", use_container_width=True)

                if submitted:
                    if new_material:
                        success, messages = st.session_state.service.add_yarn_material(new_material)
                        if success:
                            for msg in messages:
                                st.success(msg)
                            st.rerun()
                        else:
                            for msg in messages:
                                st.error(msg)
                    else:
                        st.error("Please enter a material name")

    # TAB 3: DESIGN/WEAVE TYPES (NEW)
    with tab3:
        st.subheader("🎭 Design/Weave Type Management")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("#### Current Design/Weave Types")
            designs = st.session_state.db.get_all_design_weave_types()

            if designs:
                for idx, design in enumerate(designs):
                    col_a, col_b, col_c = st.columns([3, 1, 1])

                    with col_a:
                        st.write(f"**{idx + 1}.** {design}")

                    with col_b:
                        if st.button("✏️ Edit", key=f"edit_design_{idx}", help=f"Edit {design}"):
                            st.session_state[f'editing_design_{idx}'] = True

                    with col_c:
                        if st.button("🗑️ Delete", key=f"del_design_{idx}", help=f"Delete {design}"):
                            usage_count = st.session_state.db.check_design_weave_type_usage(design)
                            if usage_count > 0:
                                st.warning(f"⚠️ Cannot delete! '{design}' is used in {usage_count} records")
                            else:
                                if st.session_state.db.delete_design_weave_type(design):
                                    st.success(f"Deleted: {design}")
                                    st.rerun()

                    if st.session_state.get(f'editing_design_{idx}', False):
                        with st.form(f"edit_form_design_{idx}"):
                            new_name = st.text_input("New Design Name", value=design)
                            col_save, col_cancel = st.columns(2)

                            with col_save:
                                if st.form_submit_button("💾 Save"):
                                    if st.session_state.db.update_design_weave_type(design, new_name):
                                        st.success(f"Updated to: {new_name}")
                                        st.session_state[f'editing_design_{idx}'] = False
                                        st.rerun()

                            with col_cancel:
                                if st.form_submit_button("❌ Cancel"):
                                    st.session_state[f'editing_design_{idx}'] = False
                                    st.rerun()
            else:
                st.info("No design/weave types available")

        with col2:
            st.markdown("#### Add New Design")
            with st.form("add_design_form"):
                new_design = st.text_input("Design Name")
                submitted = st.form_submit_button("➕ Add", use_container_width=True)

                if submitted:
                    if new_design:
                        success, messages = st.session_state.service.add_design_weave_type(new_design)
                        if success:
                            for msg in messages:
                                st.success(msg)
                            st.rerun()
                        else:
                            for msg in messages:
                                st.error(msg)
                    else:
                        st.error("Please enter a design name")

        # TAB 4: WARPERS (NEW - Task #2)
        with tab4:
            st.subheader("👷 Warper Management")

            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown("#### Current Warpers")
                warpers = st.session_state.db.get_all_warpers()

                if warpers:
                    for idx, warper in enumerate(warpers):
                        col_a, col_b, col_c = st.columns([3, 1, 1])

                        with col_a:
                            st.write(f"**{idx + 1}.** {warper}")

                        with col_b:
                            if st.button("✏️ Edit", key=f"edit_warper_{idx}", help=f"Edit {warper}"):
                                st.session_state[f'editing_warper_{idx}'] = True

                        with col_c:
                            if st.button("🗑️ Delete", key=f"del_warper_{idx}", help=f"Delete {warper}"):
                                usage_count = st.session_state.db.check_warper_usage(warper)
                                if usage_count > 0:
                                    st.warning(f"⚠️ Cannot delete! '{warper}' is used in {usage_count} records")
                                else:
                                    if st.session_state.db.delete_warper(warper):
                                        st.success(f"Deleted: {warper}")
                                        st.rerun()

                        if st.session_state.get(f'editing_warper_{idx}', False):
                            with st.form(f"edit_form_warper_{idx}"):
                                new_name = st.text_input("New Warper Name", value=warper)
                                col_save, col_cancel = st.columns(2)

                                with col_save:
                                    if st.form_submit_button("💾 Save"):
                                        if st.session_state.db.update_warper(warper, new_name):
                                            st.success(f"Updated to: {new_name}")
                                            st.session_state[f'editing_warper_{idx}'] = False
                                            st.rerun()

                                with col_cancel:
                                    if st.form_submit_button("❌ Cancel"):
                                        st.session_state[f'editing_warper_{idx}'] = False
                                        st.rerun()
                else:
                    st.info("No warpers available")

            with col2:
                st.markdown("#### Add New Warper")
                with st.form("add_warper_form"):
                    new_warper = st.text_input("Warper Name")
                    submitted = st.form_submit_button("➕ Add", use_container_width=True)

                    if submitted:
                        if new_warper:
                            success, messages = st.session_state.service.add_warper(new_warper)
                            if success:
                                for msg in messages:
                                    st.success(msg)
                                st.rerun()
                            else:
                                for msg in messages:
                                    st.error(msg)
                        else:
                            st.error("Please enter a warper name")

        # TAB 5: REED TYPES (NEW - Task #7)
        with tab5:
            st.subheader("🔧 Reed Type Management")

            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown("#### Current Reed Types")
                reed_types = st.session_state.db.get_all_reed_types()

                if reed_types:
                    for idx, reed in enumerate(reed_types):
                        col_a, col_b, col_c = st.columns([3, 1, 1])

                        with col_a:
                            st.write(f"**{idx + 1}.** {reed}")

                        with col_b:
                            if st.button("✏️ Edit", key=f"edit_reed_{idx}", help=f"Edit {reed}"):
                                st.session_state[f'editing_reed_{idx}'] = True

                        with col_c:
                            if st.button("🗑️ Delete", key=f"del_reed_{idx}", help=f"Delete {reed}"):
                                usage_count = st.session_state.db.check_reed_type_usage(reed)
                                if usage_count > 0:
                                    st.warning(f"⚠️ Cannot delete! '{reed}' is used in {usage_count} records")
                                else:
                                    if st.session_state.db.delete_reed_type(reed):
                                        st.success(f"Deleted: {reed}")
                                        st.rerun()

                        if st.session_state.get(f'editing_reed_{idx}', False):
                            with st.form(f"edit_form_reed_{idx}"):
                                new_name = st.text_input("New Reed Type Name", value=reed)
                                col_save, col_cancel = st.columns(2)

                                with col_save:
                                    if st.form_submit_button("💾 Save"):
                                        if st.session_state.db.update_reed_type(reed, new_name):
                                            st.success(f"Updated to: {new_name}")
                                            st.session_state[f'editing_reed_{idx}'] = False
                                            st.rerun()

                                with col_cancel:
                                    if st.form_submit_button("❌ Cancel"):
                                        st.session_state[f'editing_reed_{idx}'] = False
                                        st.rerun()
                else:
                    st.info("No reed types available")

            with col2:
                st.markdown("#### Add New Reed Type")
                with st.form("add_reed_form"):
                    new_reed = st.text_input("Reed Type Name")
                    submitted = st.form_submit_button("➕ Add", use_container_width=True)

                    if submitted:
                        if new_reed:
                            success, messages = st.session_state.service.add_reed_type(new_reed)
                            if success:
                                for msg in messages:
                                    st.success(msg)
                                st.rerun()
                            else:
                                for msg in messages:
                                    st.error(msg)
                        else:
                            st.error("Please enter a reed type name")

    # TAB 6: JOB WORKERS - WITH USAGE WARNING
    with tab6:
        st.subheader("👨‍🏭 Job Worker Management")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("#### Current Job Workers")
            workers = st.session_state.db.get_all_job_workers()

            if workers:
                for idx, worker in enumerate(workers):
                    worker_details = st.session_state.db.get_job_worker_details(worker)
                    usage_count = st.session_state.db.check_job_worker_usage(worker)

                    col_a, col_b, col_c = st.columns([3, 1, 1])

                    with col_a:
                        contact = worker_details['contact_number'] if worker_details and worker_details[
                            'contact_number'] else "N/A"
                        st.write(f"**{idx + 1}.** {worker} - 📞 {contact}")

                    with col_b:
                        if st.button("✏️ Edit", key=f"edit_worker_{idx}", help=f"Edit {worker}"):
                            st.session_state[f'editing_worker_{idx}'] = True

                    with col_c:
                        if st.button("🗑️ Delete", key=f"del_worker_{idx}", help=f"Delete {worker}"):
                            # Check usage before deleting
                            if usage_count > 0:
                                st.error(f"⚠️ Cannot delete! '{worker}' is used in {usage_count} records")
                            else:
                                if st.session_state.db.delete_job_worker(worker):
                                    st.success(f"✅ Deleted: {worker}")
                                    st.rerun()
                                else:
                                    st.error("❌ Failed to delete worker")

                    # Show usage warning if worker is being used
                    # if usage_count > 0:
                    #     st.warning(f"⚠️ This worker is used in **{usage_count} records**")

                    if st.session_state.get(f'editing_worker_{idx}', False):
                        with st.form(f"edit_form_worker_{idx}"):
                            if worker_details:
                                new_name = st.text_input("Worker Name", value=worker_details['worker_name'])
                                new_contact = st.text_input("Contact Number",
                                                            value=worker_details['contact_number'] or "")
                                new_gst = st.text_input("GST Number", value=worker_details['gst_number'] or "")
                                new_aadhar = st.text_input("Aadhar Number", value=worker_details['aadhar_number'] or "")
                            else:
                                new_name = st.text_input("Worker Name", value=worker)
                                new_contact = st.text_input("Contact Number")
                                new_gst = st.text_input("GST Number")
                                new_aadhar = st.text_input("Aadhar Number")

                            col_save, col_cancel = st.columns(2)

                            with col_save:
                                if st.form_submit_button("💾 Save"):
                                    success, messages = st.session_state.service.update_job_worker(
                                        worker, new_name, new_contact, new_gst, new_aadhar
                                    )
                                    if success:
                                        for msg in messages:
                                            st.success(msg)
                                        st.session_state[f'editing_worker_{idx}'] = False
                                        st.rerun()
                                    else:
                                        for msg in messages:
                                            st.error(msg)

                            with col_cancel:
                                if st.form_submit_button("❌ Cancel"):
                                    st.session_state[f'editing_worker_{idx}'] = False
                                    st.rerun()
            else:
                st.info("No job workers available")

        with col2:
            st.markdown("#### Add New Worker")
            with st.form("add_worker_form"):
                new_worker = st.text_input("Worker Name *")
                contact_number = st.text_input("Contact Number")
                gst_number = st.text_input("GST Number")
                aadhar_number = st.text_input("Aadhar Number")
                submitted = st.form_submit_button("➕ Add", use_container_width=True)

                if submitted:
                    if new_worker:
                        success, messages = st.session_state.service.add_job_worker(
                            new_worker, contact_number, gst_number, aadhar_number
                        )
                        if success:
                            for msg in messages:
                                st.success(msg)
                            st.rerun()
                        else:
                            for msg in messages:
                                st.error(msg)
                    else:
                        st.error("Please enter a worker name")

    # TAB 7: PRODUCT CATEGORIES - WITH USAGE WARNING
    with tab7:
        st.subheader("📦 Product Category Management")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("#### Current Product Categories")
            categories = st.session_state.db.get_all_product_categories()

            if categories:
                for idx, category in enumerate(categories):
                    usage_count = st.session_state.db.check_product_category_usage(category)

                    col_a, col_b, col_c = st.columns([3, 1, 1])

                    with col_a:
                        st.write(f"**{idx + 1}.** {category}")

                    with col_b:
                        if st.button("✏️ Edit", key=f"edit_category_{idx}", help=f"Edit {category}"):
                            st.session_state[f'editing_category_{idx}'] = True

                    with col_c:
                        if st.button("🗑️ Delete", key=f"del_category_{idx}", help=f"Delete {category}"):
                            # Check usage before deleting
                            if usage_count > 0:
                                st.error(f"⚠️ Cannot delete! '{category}' is used in {usage_count} records")
                            else:
                                if st.session_state.db.delete_product_category(category):
                                    st.success(f"✅ Deleted: {category}")
                                    st.rerun()
                                else:
                                    st.error("❌ Failed to delete category")

                    # Show usage warning if category is being used
                    # if usage_count > 0:
                    #     st.warning(f"⚠️ This category is used in **{usage_count} records**")

                    if st.session_state.get(f'editing_category_{idx}', False):
                        with st.form(f"edit_form_category_{idx}"):
                            new_name = st.text_input("New Category Name", value=category)
                            col_save, col_cancel = st.columns(2)

                            with col_save:
                                if st.form_submit_button("💾 Save"):
                                    if st.session_state.db.update_product_category(category, new_name):
                                        st.success(f"✅ Updated to: {new_name}")
                                        st.session_state[f'editing_category_{idx}'] = False
                                        st.rerun()
                                    else:
                                        st.error("❌ Failed to update category")

                            with col_cancel:
                                if st.form_submit_button("❌ Cancel"):
                                    st.session_state[f'editing_category_{idx}'] = False
                                    st.rerun()
            else:
                st.info("No product categories available")

        with col2:
            st.markdown("#### Add New Category")
            with st.form("add_category_form"):
                new_category = st.text_input("Category Name")
                submitted = st.form_submit_button("➕ Add", use_container_width=True)

                if submitted:
                    if new_category:
                        success, messages = st.session_state.service.add_product_category(new_category)
                        if success:
                            for msg in messages:
                                st.success(msg)
                            st.rerun()
                        else:
                            for msg in messages:
                                st.error(msg)
                    else:
                        st.error("Please enter a category name")

# ========================================
# FOOTER
# ========================================
st.sidebar.markdown("---")
st.sidebar.info("💡 **AIFuturix's WARP & WEFT Management System**")