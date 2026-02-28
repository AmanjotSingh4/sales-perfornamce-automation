import matplotlib.pyplot as plt
import pandas as pd


def plot_monthly_trends(df):
    df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

    monthly_revenue = df.groupby("Year-Month")["Total Revenue"].sum()
    monthly_profit = df.groupby("Year-Month")["Total Profit"].sum()

    # Revenue Chart
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    monthly_revenue.plot(ax=ax1, color="#4CAF50", linewidth=2)
    ax1.set_ylabel("Revenue")
    ax1.set_title("Monthly Revenue")

    # Profit Chart
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    monthly_profit.plot(ax=ax2, color="#FF6B6B", linewidth=2)
    ax2.set_ylabel("Profit")
    ax2.set_title("Monthly Profit")

    return fig1, fig2


def plot_sales_channel(df):
    sales_channel_revenue = df.groupby("Sales Channel")["Total Revenue"].sum()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    sales_channel_revenue.plot(
        kind="bar",
        ax=ax,
        color=["#4CAF50", "#2196F3"]
    )

    ax.set_ylabel("Total Revenue")
    ax.set_title("Revenue by Sales Channel")

    return fig


def plot_revenue_by_region(df):
    revenue_by_region = (
        df.groupby("Region")["Total Revenue"]
        .sum()
        .sort_values(ascending=True)
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    revenue_by_region.plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Total Revenue")
    ax.set_ylabel("Region")
    ax.set_title("Regional Revenue Comparison")

    return fig