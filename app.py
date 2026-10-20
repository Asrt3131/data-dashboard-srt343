# app.py
import streamlit as st
import plotly.express as px
import pandas as pd
from src.etl import load_and_clean_data

# ---------- Page configuration ----------
st.set_page_config(
    page_title="Sales Intelligence | A_srt343",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Professional custom styling ----------
st.markdown("""
<style>
    .block-container { padding-top: 2rem; }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1E2530 0%, #0E1117 100%);
        border: 1px solid #2E3A4A;
        border-radius: 12px;
        padding: 15px 20px;
    }
    div[data-testid="stMetricLabel"] { font-size: 0.85rem; color: #8899AA; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #00D4AA; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1E2530;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .main-header { font-size: 2.3rem; color: #00D4AA; text-align: center; margin-bottom: 0.5rem; }
    .footer { text-align: center; font-size: 0.9rem; color: gray; margin-top: 50px; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ---------- Load data (cached) ----------
@st.cache_data
def get_data():
    return load_and_clean_data()


df = get_data()


# ---------- Navigation ----------
pg = st.navigation([
    st.Page("pages/1_📊_Overview.py",  title="Overview", icon="📊", default=True),
    st.Page("pages/2_📈_Trends.py",    title="Trends",   icon="📈"),
    st.Page("pages/3_🗺️_Geography.py", title="Geography", icon="🗺️"),
    st.Page("pages/4_🔍_Explorer.py",  title="Data Explorer", icon="🔍"),
])


# ---------- Sidebar Branding + Global filters ----------
with st.sidebar:
    st.markdown("### 📊 Sales Intelligence")
    st.caption("Superstore sales analytics dashboard")
    st.divider()

    st.markdown("#### 🔍 Filters")
    regions = st.multiselect(
        "Region",
        options=df["Region"].unique(),
        default=df["Region"].unique(),
        key="filter_regions",
    )
    categories = st.multiselect(
        "Category",
        options=df["Category"].unique(),
        default=df["Category"].unique(),
        key="filter_categories",
    )

    st.divider()
    st.caption("Built by **A_srt343**")
    st.caption("Instagram: [@project_srt343](https://instagram.com/project_srt343)")


# ---------- Global filtering (stored in session_state so pages can access it) ----------
df_filtered = df[
    (df["Region"].isin(regions)) & (df["Category"].isin(categories))
].copy()

# Store in session_state for use across pages
st.session_state["df_filtered"] = df_filtered
st.session_state["regions"] = regions
st.session_state["categories"] = categories


# ---------- Run the selected page ----------
pg.run()


# ---------- Footer ----------
st.markdown("""
<div class="footer">
    Built with ❤️ by <b>A_srt343</b><br>
    Instagram: @project_srt343
</div>
""", unsafe_allow_html=True)