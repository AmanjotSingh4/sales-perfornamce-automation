import pandas as pd
from grok_client import ask_groq


def compute_kpis(df):
    total_revenue = df["Total Revenue"].sum()
    total_profit = df["Total Profit"].sum()
    avg_profit = df["Total Profit"].mean()
    profit_margin = (total_profit / total_revenue) * 100

    most_profitable_region = (
        df.groupby("Region")["Total Profit"]
        .sum()
        .idxmax()
    )

    most_profitable_item = (
        df.groupby("Item Type")["Total Profit"]
        .sum()
        .idxmax()
    )

    revenue_by_channel = (
        df.groupby("Sales Channel")["Total Revenue"]
        .sum()
    )

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "avg_profit": avg_profit,
        "profit_margin": profit_margin,
        "most_profitable_region": most_profitable_region,
        "most_profitable_item": most_profitable_item,
        "revenue_by_channel": revenue_by_channel,
    }


def build_context(kpis):
    context = f"""
    Sales Performance Overview:

    Total Revenue: {kpis['total_revenue']:,.2f}
    Total Profit: {kpis['total_profit']:,.2f}
    Average Profit per Order: {kpis['avg_profit']:,.2f}
    Profit Margin: {kpis['profit_margin']:.2f}%

    Most Profitable Region: {kpis['most_profitable_region']}
    Most Profitable Item Type: {kpis['most_profitable_item']}

    Revenue by Channel:
    {kpis['revenue_by_channel'].to_string()}
    """
    return context


def generate_ai_summary(context):
    prompt = f"""
    You are a senior business analyst.
    Based on the following sales data summary,
    write a concise executive-level strategic summary
    with insights and recommendations.

    {context}
    """

    response = ask_groq(prompt)
    return response