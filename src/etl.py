# src/etl.py
import pandas as pd
import numpy as np

def load_and_clean_data(path: str = "data/superstore.csv") -> pd.DataFrame:
    """Load and professionally clean the Superstore dataset with extra features"""
    df = pd.read_csv(path, encoding="latin-1")
    
    # --- Basic cleaning ---
    df.dropna(subset=["Sales", "Profit", "Order Date"], inplace=True)
    df.drop_duplicates(inplace=True)
    
    # --- Date conversion ---
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df.dropna(subset=["Order Date"], inplace=True)
    
    # --- Feature Engineering ---
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Quarter"] = df["Order Date"].dt.quarter
    df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)
    df["DayOfWeek"] = df["Order Date"].dt.day_name()
    
    # --- Financial calculations ---
    df["Profit Margin"] = np.where(df["Sales"] > 0, df["Profit"] / df["Sales"], 0)
    df["Is Profitable"] = df["Profit"] > 0
    df["Discount Level"] = pd.cut(
        df["Discount"], 
        bins=[-0.01, 0, 0.2, 0.4, 1.0], 
        labels=["No Discount", "Low (0-20%)", "Medium (20-40%)", "High (40%+)"]
    )
    
    # --- Customer segmentation ---
    df["Customer Segment"] = df["Segment"].fillna("Unknown")
    
    return df


def get_kpis(df: pd.DataFrame) -> dict:
    """Calculate key KPIs"""
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()
    avg_order_value = total_sales / total_orders if total_orders > 0 else 0
    profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    
    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "avg_order_value": avg_order_value,
        "profit_margin": profit_margin,
    }