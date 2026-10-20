# src/charts.py
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Custom color palette
COLORS = ["#00D4AA", "#FF6B6B", "#4ECDC4", "#FFE66D", "#A8E6CF", "#FF8C94"]

def sales_by_category(df: pd.DataFrame) -> go.Figure:
    agg = df.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=True)
    fig = px.bar(
        agg, x="Sales", y="Category", orientation="h",
        color="Sales", color_continuous_scale="Teal",
        text_auto=".2s", template="plotly_dark"
    )
    fig.update_layout(
        height=350, showlegend=False, 
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis_title="", yaxis_title="",
        coloraxis_showscale=False
    )
    fig.update_traces(textposition="outside")
    return fig


def monthly_trend(df: pd.DataFrame) -> go.Figure:
    agg = df.groupby("YearMonth", as_index=False)["Sales"].sum()
    agg = agg.sort_values("YearMonth")
    fig = px.area(
        agg, x="YearMonth", y="Sales",
        template="plotly_dark", color_discrete_sequence=[COLORS[0]]
    )
    fig.update_layout(
        height=350, margin=dict(l=0, r=0, t=10, b=0),
        xaxis_title="", yaxis_title="Sales ($)",
        hovermode="x unified"
    )
    fig.update_xaxes(nticks=12)
    return fig


def profit_by_region(df: pd.DataFrame) -> go.Figure:
    agg = df.groupby("Region", as_index=False)["Profit"].sum()
    fig = px.pie(
        agg, names="Region", values="Profit", hole=0.55,
        template="plotly_dark", color_discrete_sequence=COLORS
    )
    fig.update_layout(
        height=350, margin=dict(l=0, r=0, t=10, b=0),
        legend=dict(orientation="h", yanchor="bottom", y=-0.1)
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig


def discount_impact(df: pd.DataFrame) -> go.Figure:
    """Analyzing the impact of discount on profit — this is what a real analyst shows"""
    agg = df.groupby("Discount Level", observed=True, as_index=False).agg(
        avg_profit=("Profit", "mean"),
        total_sales=("Sales", "sum")
    )
    fig = px.bar(
        agg, x="Discount Level", y="avg_profit",
        color="avg_profit", color_continuous_scale="RdYlGn",
        template="plotly_dark", text_auto=".0f"
    )
    fig.update_layout(
        height=350, showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis_title="", yaxis_title="Avg Profit ($)",
        coloraxis_showscale=False
    )
    return fig


def top_products(df: pd.DataFrame, n: int = 10) -> go.Figure:
    agg = df.groupby("Product Name", as_index=False)["Sales"].sum()
    agg = agg.nlargest(n, "Sales").sort_values("Sales")
    fig = px.bar(
        agg, x="Sales", y="Product Name", orientation="h",
        template="plotly_dark", color_discrete_sequence=[COLORS[3]]
    )
    fig.update_layout(
        height=400, margin=dict(l=0, r=0, t=10, b=0),
        xaxis_title="", yaxis_title="",
        yaxis=dict(tickfont=dict(size=10))
    )
    return fig


def sales_heatmap(df: pd.DataFrame) -> go.Figure:
    """Sales heatmap by month and year — visual and professional"""
    pivot = df.pivot_table(index="Month", columns="Year", values="Sales", aggfunc="sum")
    fig = px.imshow(
        pivot, aspect="auto", color_continuous_scale="Teal",
        template="plotly_dark", text_auto=".0s"
    )
    fig.update_layout(
        height=300, margin=dict(l=0, r=0, t=10, b=0),
        xaxis_title="", yaxis_title=""
    )
    return fig