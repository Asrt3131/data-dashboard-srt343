# src/etl.py
import pandas as pd
import os

def load_and_clean_data(path: str = "data/superstore.csv") -> pd.DataFrame:
    """بارگذاری و تمیزکاری دیتاست Superstore"""
    df = pd.read_csv(path, encoding="latin-1")
    
    # حذف ردیف‌های خالی و تکراری
    df.dropna(subset=["Sales", "Profit", "Order Date"], inplace=True)
    df.drop_duplicates(inplace=True)
    
    # تبدیل تاریخ
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df.dropna(subset=["Order Date"], inplace=True)
    
    # استخراج سال و ماه
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print(f"✅ داده تمیز شد: {len(df)} رکورد")
    print(df.head())