import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use("Agg")


def load_data():
    file_path = "dataset/online_retail_II.csv"

    df = pd.read_csv(
        file_path,
        encoding="ISO-8859-1",
        sep=",",
        engine="python"
    )

    # Remove missing Customer IDs
    df = df.dropna(subset=["Customer ID"])

    # Remove cancelled invoices
    df = df[~df["Invoice"].astype(str).str.startswith("C")]

    # Remove invalid Quantity and Price
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing product descriptions
    df = df.dropna(subset=["Description"])

    # Remove blank product descriptions
    df = df[df["Description"].str.strip() != ""]

    # Standardize product names
    df["Description"] = df["Description"].str.upper().str.strip()

    # Convert InvoiceDate
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        dayfirst=True,
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["InvoiceDate"])

    # Feature Engineering
    df["TotalPrice"] = df["Quantity"] * df["Price"]
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month_name()
    df["MonthNo"] = df["InvoiceDate"].dt.month

    return df

def sales_summary(df):
    total_sales = df["TotalPrice"].sum()
    total_orders = df["Invoice"].nunique()

    return {
        "Total Sales": round(total_sales, 2),
        "Total Orders": total_orders,
        "Total Customers": df["Customer ID"].nunique(),
        "Average Order Value": round(total_sales / total_orders, 2)
    }


def top_products(df):
    return (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def country_sales(df):
    return (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def customer_segments(df):
    spending = df.groupby("Customer ID")["TotalPrice"].sum()

    return {
        "High Value": (spending > 1000).sum(),
        "Medium Value": ((spending > 300) & (spending <= 1000)).sum(),
        "Low Value": (spending <= 300).sum()
    }

def top_customers(df):

    return (
        df.groupby("Customer ID")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
def repeat_customers(df):

    customer_orders = df.groupby("Customer ID")["Invoice"].nunique()

    return {
        "Repeat Customers": int((customer_orders > 1).sum()),
        "New Customers": int((customer_orders == 1).sum())
    }

def monthly_sales(df):

    monthly = (
        df.groupby(["Year", "MonthNo", "Month"])["TotalPrice"]
        .sum()
        .reset_index()
        .sort_values(["Year", "MonthNo"])
    )

    monthly["MonthLabel"] = (
        monthly["Month"].str[:3] +
        "-" +
        monthly["Year"].astype(str)
    )

    return monthly


def create_charts(df):

    os.makedirs("charts", exist_ok=True)

    # Top Products
    plt.figure(figsize=(10, 5))
    top_products(df).plot(kind="bar")
    plt.title("Top Selling Products")
    plt.tight_layout()
    plt.savefig("charts/top_products.png")
    plt.close()

    # Country Sales
    plt.figure(figsize=(10, 5))
    country_sales(df).plot(kind="bar")
    plt.title("Country Sales")
    plt.tight_layout()
    plt.savefig("charts/country_sales.png")
    plt.close()

    # Monthly Sales
    monthly = monthly_sales(df)

    plt.figure(figsize=(12, 5))
    plt.plot(
        monthly["MonthLabel"],
        monthly["TotalPrice"],
        marker="o"
    )
    plt.xticks(rotation=45)
    plt.title("Monthly Sales Trend")
    plt.tight_layout()
    plt.savefig("charts/monthly_sales.png")
    plt.close()


# ==========================================================
# Executive Summary
# ==========================================================

def executive_summary(df):

    total_sales = df["TotalPrice"].sum()

    top_country = (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .idxmax()
    )

    top_product = (
        df.groupby("Description")["Quantity"]
        .sum()
        .idxmax()
    )

    spending = df.groupby("Customer ID")["TotalPrice"].sum()

    high = (spending > 1000).sum()
    medium = ((spending > 300) & (spending <= 1000)).sum()
    low = (spending <= 300).sum()

    dominant_segment = max(
        {
            "High Value": high,
            "Medium Value": medium,
            "Low Value": low
        },
        key={
            "High Value": high,
            "Medium Value": medium,
            "Low Value": low
        }.get
    )

    return [

f"Business generated total revenue of £ {total_sales:,.2f}, indicating strong overall sales performance."
    f"{top_country} is the highest revenue generating market and should remain a primary business focus.",

    f"'{top_product}' is the best-selling product and has high demand among customers.",

    f"The largest customer group belongs to the {dominant_segment} segment, showing the current customer distribution.",

    "Increase inventory for high-demand products, strengthen customer retention programs, and promote underperforming products through targeted marketing campaigns."

]