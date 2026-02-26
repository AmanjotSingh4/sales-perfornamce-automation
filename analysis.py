def compute_metrics(df):
    total_revenue = df['Total Revenue'].sum()
    total_profit = df['Total Profit'].sum()
    avg_profit = df['Total Profit'].mean()

    most_profitable_region = (
        df.groupby('Region')['Total Profit']
        .sum()
        .idxmax()
    )

    most_profitable_item = (
        df.groupby('Item Type')['Total Profit']
        .sum()
        .idxmax()
    )

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "avg_profit": avg_profit,
        "most_profitable_region": most_profitable_region,
        "most_profitable_item": most_profitable_item
    }