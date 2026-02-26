import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

from preprocess import clean_data
from analysis import compute_metrics

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Performance Dashboard")
st.caption("Upload a transactional sales dataset to generate automated performance insights.")

st.markdown("---")

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload your sales CSV file",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Please upload a CSV file to begin analysis.")
    st.stop()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv(uploaded_file)

# ---------------------------------------------------
# REQUIRED COLUMN VALIDATION
# ---------------------------------------------------
required_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Date",
    "Ship Date",
    "Total Revenue",
    "Total Profit"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(
        f"This dataset must contain the following columns: {', '.join(required_columns)}"
    )
    st.stop()

# ---------------------------------------------------
# CLEAN DATA
# ---------------------------------------------------
df = clean_data(df)

# ---------------------------------------------------
# COMPUTE METRICS
# ---------------------------------------------------
metrics = compute_metrics(df)

total_revenue = metrics["total_revenue"]
total_profit = metrics["total_profit"]
avg_profit = metrics["avg_profit"]
most_profitable_region = metrics["most_profitable_region"]
most_profitable_item = metrics["most_profitable_item"]

# ---------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------
st.markdown("## 📊 Executive Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Average Profit per Order", f"${avg_profit:,.2f}")

st.success(f"""
**Most Profitable Region:** {most_profitable_region}  
**Most Profitable Item Type:** {most_profitable_item}
""")

st.markdown("---")

# ---------------------------------------------------
# MONTHLY TRENDS
# ---------------------------------------------------
df['Year-Month'] = pd.to_datetime(df['Order Date']).dt.to_period('M')

monthly_revenue = df.groupby('Year-Month')['Total Revenue'].sum()
monthly_profit = df.groupby('Year-Month')['Total Profit'].sum()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Revenue")
    fig, ax = plt.subplots(figsize=(6, 3))
    monthly_revenue.plot(ax=ax)
    ax.set_ylabel("Revenue")
    ax.tick_params(axis='x', rotation=45)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("📉 Monthly Profit")
    fig, ax = plt.subplots(figsize=(6, 3))
    monthly_profit.plot(ax=ax)
    ax.set_ylabel("Profit")
    ax.tick_params(axis='x', rotation=45)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    st.pyplot(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# SALES CHANNEL PERFORMANCE
# ---------------------------------------------------
st.subheader("🛒 Revenue by Sales Channel")

sales_by_channel = df.groupby('Sales Channel')['Total Revenue'].sum()

fig, ax = plt.subplots(figsize=(5, 3))
sales_by_channel.plot(kind='bar', ax=ax)
ax.set_ylabel("Revenue")
ax.tick_params(axis='x', rotation=0)
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
st.pyplot(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# TOP 5 COUNTRIES
# ---------------------------------------------------
st.subheader("🌍 Top 5 Countries by Revenue")

top_countries = (
    df.groupby('Country')['Total Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig, ax = plt.subplots(figsize=(6, 3))
top_countries.plot(kind='bar', ax=ax)
ax.set_ylabel("Revenue")
ax.tick_params(axis='x', rotation=45)
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
st.pyplot(fig, use_container_width=True)