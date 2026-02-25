import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Performance Dashboard")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv("sales.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'])

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("🔎 Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

channel_filter = st.sidebar.multiselect(
    "Select Sales Channel",
    options=df['Sales Channel'].unique(),
    default=df['Sales Channel'].unique()
)

df = df[
    (df['Region'].isin(region_filter)) &
    (df['Sales Channel'].isin(channel_filter))
]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
total_revenue = df['Total Revenue'].sum()
total_profit = df['Total Profit'].sum()
avg_profit = df['Total Profit'].mean()
profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Avg Profit / Order", f"${avg_profit:,.2f}")
col4.metric("Profit Margin", f"{profit_margin:.2f}%")

st.markdown("---")

# ---------------------------------------------------
# MONTHLY TRENDS
# ---------------------------------------------------
df['Year-Month'] = df['Order Date'].dt.to_period('M')
monthly_revenue = df.groupby('Year-Month')['Total Revenue'].sum()
monthly_profit = df.groupby('Year-Month')['Total Profit'].sum()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Revenue")
    fig, ax = plt.subplots(figsize=(6, 3))
    monthly_revenue.plot(ax=ax)
    ax.set_ylabel("Revenue")
    ax.set_xlabel("")
    ax.tick_params(axis='x', rotation=45)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("📉 Monthly Profit")
    fig, ax = plt.subplots(figsize=(6, 3))
    monthly_profit.plot(ax=ax)
    ax.set_ylabel("Profit")
    ax.set_xlabel("")
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
ax.set_xlabel("")
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
ax.set_xlabel("")
ax.tick_params(axis='x', rotation=45)
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
st.pyplot(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# PROFITABILITY INSIGHTS
# ---------------------------------------------------
st.subheader("🏆 Profitability Insights")

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

col1, col2 = st.columns(2)

col1.info(f"Most Profitable Region: **{most_profitable_region}**")
col2.info(f"Most Profitable Item Type: **{most_profitable_item}**")