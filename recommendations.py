def generate_recommendations(df):

    recommendations = []

    # ==========================
    # Top Revenue Country
    # ==========================

    country_sales = (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
    )

    top_country = country_sales.index[0]

    recommendations.append(
        f"{top_country} contributes the highest revenue. Continue investing in this market while expanding marketing efforts in other regions to reduce dependency on a single market."
    )

    # ==========================
    # Best Selling Product
    # ==========================

    product_sales = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    best_product = product_sales.index[0]

    recommendations.append(
        f"'{best_product}' is the highest-selling product. Maintain sufficient inventory and consider bundling it with complementary products to increase revenue."
    )

    # ==========================
    # Average Order Value
    # ==========================

    avg_order = (
        df["TotalPrice"].sum()
        / df["Invoice"].nunique()
    )

    if avg_order < 500:

        recommendations.append(
            "Average Order Value is relatively low. Introduce product bundles, cross-selling and discount offers to encourage customers to spend more per purchase."
        )

    else:

        recommendations.append(
            "Average Order Value is healthy. Continue promoting premium products and bundle offers to sustain customer spending."
        )

    # ==========================
    # Customer Segmentation
    # ==========================

    customer_spending = (
        df.groupby("Customer ID")["TotalPrice"]
        .sum()
    )

    high = (customer_spending > 1000).sum()
    medium = (
        (customer_spending > 300) &
        (customer_spending <= 1000)
    ).sum()
    low = (customer_spending <= 300).sum()

    if low > medium:

        recommendations.append(
            "Most customers belong to the Low Value segment. Launch personalized promotions and loyalty campaigns to convert them into repeat and higher-value customers."
        )

    elif medium > high:

        recommendations.append(
            "A large number of Medium Value customers present an opportunity for upselling. Offer premium products and exclusive discounts to increase customer lifetime value."
        )

    else:

        recommendations.append(
            "High Value customers contribute significantly to revenue. Strengthen loyalty programs and provide exclusive benefits to retain them."
        )

    # ==========================
    # Monthly Sales Trend
    # ==========================

    monthly = (
        df.groupby(df["InvoiceDate"].dt.month_name())["TotalPrice"]
        .sum()
    )

    peak_month = monthly.idxmax()

    recommendations.append(
        f"Sales peak during {peak_month}. Prepare inventory and marketing campaigns in advance to maximize seasonal demand."
    )

    # ==========================
    # Low Selling Products
    # ==========================

    low_products = (
        product_sales.sort_values()
        .head(5)
        .index
        .tolist()
    )

    recommendations.append(
        "Review pricing, product placement and promotional strategies for low-performing products such as "
        + ", ".join(low_products[:3])
        + " to improve their sales performance."
    )

    return recommendations