# app.py
import streamlit as st
import plotly.express as px
import pandas as pd
from src.etl import load_and_clean_data

# ---------- تنظیمات صفحه ----------
st.set_page_config(
    page_title="داشبورد تحلیل فروش | A_srt343",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- استایل سفارشی ----------
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #1f77b4; text-align: center; }
    .footer { text-align: center; font-size: 0.9rem; color: gray; margin-top: 50px; }
</style>
""", unsafe_allow_html=True)

# ---------- بارگذاری داده (کش‌شده) ----------
@st.cache_data
def get_data():
    return load_and_clean_data()

df = get_data()

# ---------- هدر ----------
st.markdown('<h1 class="main-header">📊 داشبورد تحلیل فروش Superstore</h1>', unsafe_allow_html=True)
st.markdown("**ساخته شده توسط A_srt343** | [Instagram](https://instagram.com/project_srt343)")

# ---------- فیلترهای کناری ----------
st.sidebar.header("🔍 فیلترها")
regions = st.sidebar.multiselect("منطقه", options=df["Region"].unique(), default=df["Region"].unique())
categories = st.sidebar.multiselect("دسته‌بندی", options=df["Category"].unique(), default=df["Category"].unique())

df_filtered = df[(df["Region"].isin(regions)) & (df["Category"].isin(categories))]

# ---------- KPI ها ----------
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 کل فروش", f"${df_filtered['Sales'].sum():,.0f}")
col2.metric("📈 کل سود", f"${df_filtered['Profit'].sum():,.0f}")
col3.metric("📦 تعداد سفارش", f"{len(df_filtered):,}")
col4.metric("📊 حاشیه سود", f"{(df_filtered['Profit'].sum() / df_filtered['Sales'].sum() * 100):.1f}%")

st.divider()

# ---------- نمودار ۱: فروش بر اساس دسته‌بندی ----------
st.subheader("📦 فروش بر اساس دسته‌بندی")
fig1 = px.bar(
    df_filtered.groupby("Category")["Sales"].sum().reset_index(),
    x="Category", y="Sales", color="Category",
    text_auto=".2s", template="plotly_white"
)
st.plotly_chart(fig1, use_container_width=True)

# ---------- نمودار ۲: روند فروش ماهانه ----------
st.subheader("📅 روند فروش ماهانه")
monthly = df_filtered.groupby(["Year", "Month"])["Sales"].sum().reset_index()
monthly["Date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(day=1))
fig2 = px.line(monthly, x="Date", y="Sales", markers=True, template="plotly_white")
st.plotly_chart(fig2, use_container_width=True)

# ---------- نمودار ۳: سود بر اساس منطقه ----------
st.subheader("🗺️ سود بر اساس منطقه")
fig3 = px.pie(
    df_filtered.groupby("Region")["Profit"].sum().reset_index(),
    names="Region", values="Profit", hole=0.4, template="plotly_white"
)
st.plotly_chart(fig3, use_container_width=True)

# ---------- فوتر ----------
st.markdown("""
<div class="footer">
    Built with ❤️ by A_srt343<br>
    Instagram: @project_srt343
</div>
""", unsafe_allow_html=True)