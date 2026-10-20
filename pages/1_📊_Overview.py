# pages/1_📊_Overview.py
import streamlit as st
from src.etl import load_and_clean_data, get_kpis
from src.charts import sales_by_category, profit_by_region, discount_impact

@st.cache_data(show_spinner="Loading data...")
def get_data():
    return load_and_clean_data()

df = get_data()
kpis = get_kpis(df)

# --- Header ---
st.title("📊 Sales Overview")
st.caption("Real-time analysis of Superstore sales performance")

# --- Filters ---
with st.expander("🎛️ Advanced Filters", expanded=False):
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        years = st.multiselect("Year", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
    with col_f2:
        regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
    with col_f3:
        categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))

# Apply filters
mask = df["Year"].isin(years) & df["Region"].isin(regions) & df["Category"].isin(categories)
df_f = df[mask]

# --- KPI Cards ---
st.subheader("Key Performance Indicators")
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("💰 Total Sales", f"${kpis['total_sales']/1e6:.2f}M" if kpis['total_sales'] > 1e6 else f"${kpis['total_sales']:,.0f}")
c2.metric("📈 Total Profit", f"${kpis['total_profit']/1e3:.1f}K" if kpis['total_profit'] > 1e3 else f"${kpis['total_profit']:,.0f}")
c3.metric("📦 Orders", f"{kpis['total_orders']:,}")
c4.metric("👥 Customers", f"{kpis['total_customers']:,}")
c5.metric("🎯 Profit Margin", f"{kpis['profit_margin']:.1f}%")
c6.metric("🛒 Avg Order Value", f"${kpis['avg_order_value']:,.0f}")

st.divider()

# --- Charts Row 1 ---
col_left, col_right = st.columns([1.5, 1])
with col_left:
    st.subheader("📦 Sales by Category")
    st.plotly_chart(sales_by_category(df_f), use_container_width=True)
with col_right:
    st.subheader("🗺️ Profit Share by Region")
    st.plotly_chart(profit_by_region(df_f), use_container_width=True)

# --- Chart Row 2 ---
st.subheader("💸 Impact of Discount on Average Profit")
st.plotly_chart(discount_impact(df_f), use_container_width=True)

# --- Footer ---
st.divider()
st.caption("Built with ❤️ by A_srt343 | Instagram: @project_srt343")