# pages/3_🗺️_Geography.py
import streamlit as st
import plotly.express as px
from src.etl import load_and_clean_data

@st.cache_data
def get_data():
    return load_and_clean_data()

df = get_data()

st.title("🗺️ Geographic Analysis")
st.caption("Sales performance across different US states")

# --- Map ---
state_agg = df.groupby("State", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
)

fig_map = px.choropleth(
    state_agg,
    locations="State",
    locationmode="USA-states",
    color="Sales",
    scope="usa",
    color_continuous_scale="Teal",
    template="plotly_dark",
    hover_data=["Profit", "Orders"]
)
fig_map.update_layout(height=500, margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig_map, use_container_width=True)

# --- State Ranking ---
st.subheader("🏅 State Ranking")
top_states = state_agg.nlargest(15, "Sales").sort_values("Sales")
fig_bar = px.bar(
    top_states, x="Sales", y="State", orientation="h",
    template="plotly_dark", color="Sales", color_continuous_scale="Teal",
    text_auto=".2s"
)
fig_bar.update_layout(height=450, showlegend=False, margin=dict(l=0, r=0, t=10, b=0))
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()
st.caption("Built with ❤️ by A_srt343 | Instagram: @project_srt343")