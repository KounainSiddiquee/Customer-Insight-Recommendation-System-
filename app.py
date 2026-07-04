from flask import Flask, render_template, request
import pandas as pd

from analysis.analyzer import (
    load_data,
    sales_summary,
    top_products,
    country_sales,
    customer_segments,
    top_customers,
    repeat_customers,
    executive_summary,
    create_charts,
    monthly_sales
)

from analysis.recommendations import generate_recommendations


app = Flask(__name__)


@app.route("/")
def home():

    # Load Dataset
    df = load_data()

    # Convert Date Column
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


    # ==========================
    # Filter Lists
    # ==========================

    all_countries = sorted(
        df["Country"].unique()
    )

    all_years = sorted(
        df["InvoiceDate"]
        .dt.year
        .unique()
    )


    # ==========================
    # Selected Filters
    # ==========================

    selected_country = request.args.get("country")

    selected_year = request.args.get("year")


    # Apply Country Filter

    if selected_country and selected_country != "All":

        df = df[
            df["Country"] == selected_country
        ]


    # Apply Year Filter

    if selected_year and selected_year != "All":

        df = df[
            df["InvoiceDate"].dt.year
            ==
            int(selected_year)
        ]


    # ==========================
    # Analysis
    # ==========================

    summary = sales_summary(df)

    products = top_products(df).to_dict()

    countries = country_sales(df).to_dict()

    segments = customer_segments(df)

    customers = top_customers(df).to_dict()

    repeat_data = repeat_customers(df)

    executive = executive_summary(df)

    recommendations = generate_recommendations(df)

    monthly = monthly_sales(df)


    # Generate Charts

    #create_charts(df)


    # ==========================
    # Dashboard
    # ==========================

    return render_template(

        "index.html",

        summary=summary,

        products=products,

        countries=countries,

        segments=segments,

        customers=customers,

        repeat_data=repeat_data,

        executive=executive,

        recommendations=recommendations,


        all_countries=all_countries,

        selected_country=selected_country,

        all_years=all_years,

        selected_year=selected_year,


        product_labels=list(products.keys()),

        product_values=[
            int(x) for x in products.values()
        ],


        country_labels=list(countries.keys()),

        country_values=[
            float(x) for x in countries.values()
        ],


        segment_labels=list(segments.keys()),

        segment_values=[
            int(x) for x in segments.values()
        ],


        monthly_labels=
        monthly["MonthLabel"].tolist(),

        monthly_values=[
            float(x)
            for x in monthly["TotalPrice"]
        ]

    )


if __name__ == "__main__":

    app.run(debug=False)
