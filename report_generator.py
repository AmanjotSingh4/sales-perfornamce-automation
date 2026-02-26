def generate_report(df, metrics):
    """
    Generates formatted executive report text.
    """

    total_revenue = metrics["total_revenue"]
    total_profit = metrics["total_profit"]
    avg_profit = metrics["avg_profit"]
    most_profitable_region = metrics["most_profitable_region"]
    most_profitable_item = metrics["most_profitable_item"]

    # Revenue by channel
    sales_by_channel = df.groupby('Sales Channel')['Total Revenue'].sum()

    # Top 5 countries
    top_countries = (
        df.groupby('Country')['Total Revenue']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    report = f"""
SALES PERFORMANCE ANALYSIS REPORT
=================================

EXECUTIVE SUMMARY
-----------------
Total Revenue: ${total_revenue:,.2f}
Total Profit: ${total_profit:,.2f}
Average Profit per Order: ${avg_profit:,.2f}

Most Profitable Region: {most_profitable_region}
Most Profitable Item Type: {most_profitable_item}

REVENUE BY SALES CHANNEL
------------------------
"""

    for channel, revenue in sales_by_channel.items():
        report += f"{channel}: ${revenue:,.2f}\n"

    report += "\nTOP 5 COUNTRIES BY REVENUE\n"
    report += "---------------------------\n"

    for country, revenue in top_countries.items():
        report += f"{country}: ${revenue:,.2f}\n"

    return report