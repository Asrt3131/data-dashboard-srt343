# pages/2_📈_Trends.py
import streamlit as st
from src.etl import load_and_clean_data
from src.charts import monthly_trend, sales_heatmap, top_products

@st.cache_data
def get_data():
    return load_and_clean_data()

df = get_data()

st.title("📈 Trends Analysis")
st.caption("Exploring time-based sales patterns")

# --- Time Range ---
min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    mask = (df["Order Date"].dt.date >= date_range[0]) & (df["Order Date"].dt.date <= date_range[1])
    df_f = df[mask]
else:
    df_f = df

# --- Charts ---
st.subheader("📅 Monthly Sales Trend")
st.plotly_chart(monthly_trend(df_f), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🔥 Sales Heatmap (Month × Year)")
    st.plotly_chart(sales_heatmap(df_f), use_container_width=True)
with col2:
    st.subheader("🏆 Top 10 Best-Selling Products")
    st.plotly_chart(top_products(df_f), use_container_width=True)

st.divider()
st.caption("Built with ❤️ by A_srt343 | Instagram: @project_srt343")