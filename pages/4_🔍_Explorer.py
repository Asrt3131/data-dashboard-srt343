# pages/4_🔍_Explorer.py
import streamlit as st
from src.etl import load_and_clean_data

@st.cache_data
def get_data():
    return load_and_clean_data()

df = get_data()

st.title("🔍 Data Explorer")
st.caption("Advanced filtering and raw data view")

with st.form("explorer_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        region = st.selectbox("Region", ["All"] + sorted(df["Region"].unique()))
    with col2:
        category = st.selectbox("Category", ["All"] + sorted(df["Category"].unique()))
    with col3:
        segment = st.selectbox("Customer Segment", ["All"] + sorted(df["Segment"].unique()))
    
    min_profit = st.slider("Minimum Profit", float(df["Profit"].min()), float(df["Profit"].max()), float(df["Profit"].min()))
    
    submitted = st.form_submit_button("🔎 Apply Filters", use_container_width=True)

if submitted:
    df_f = df.copy()
    if region != "All":
        df_f = df_f[df_f["Region"] == region]
    if category != "All":
        df_f = df_f[df_f["Category"] == category]
    if segment != "All":
        df_f = df_f[df_f["Segment"] == segment]
    df_f = df_f[df_f["Profit"] >= min_profit]
    
    st.success(f"✅ {len(df_f):,} records found")
    
    st.dataframe(
        df_f[["Order ID", "Order Date", "Customer Name", "Segment", "Region", "Category", "Sales", "Profit", "Profit Margin"]],
        use_container_width=True,
        height=400
    )
    
    # Download button
    csv = df_f.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download CSV",
        data=csv,
        file_name="filtered_superstore.csv",
        mime="text/csv",
        use_container_width=True
    )
else:
    st.info("👆 Set your filters and click Apply Filters.")

st.divider()
st.caption("Built with ❤️ by A_srt343 | Instagram: @project_srt343")