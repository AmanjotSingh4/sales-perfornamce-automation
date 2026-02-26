import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

from preprocess import clean_data
from analysis import compute_metrics
from report_generator import generate_report


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
# LOAD DATA SAFELY
# ---------------------------------------------------
try:
    df = pd.read_csv(uploaded_file, encoding="utf-8")
except UnicodeDecodeError:
    try:
        df = pd.read_csv(uploaded_file, encoding="latin1")
    except:
        st.error("❌ Unable to read the uploaded file. Please upload a valid CSV.")
        st.stop()
except Exception:
    st.error("❌ Unable to read the uploaded file. Please upload a valid CSV.")
    st.stop()

# Clean column names (important!)
df.columns = df.columns.str.strip()


# ---------------------------------------------------
# REQUIRED COLUMN VALIDATION
# ---------------------------------------------------
required_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Date",
    "Total Revenue",
    "Total Profit"
]

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Check required columns
        missing_cols = [col for col in required_columns if col not in df.columns]

        if missing_cols:
            st.error(
                f"❌ This dataset is missing required columns: {', '.join(missing_cols)}"
            )
            st.stop()

        # Convert Order Date safely
        try:
            df["Order Date"] = pd.to_datetime(df["Order Date"])
        except:
            st.error("❌ 'Order Date' column must contain valid date values.")
            st.stop()

    except Exception as e:
        st.error("❌ Failed to read the uploaded file. Please upload a valid CSV file.")
        st.stop()

numeric_columns = ["Total Revenue", "Total Profit"]

for col in numeric_columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        st.error(f"❌ Column '{col}' must contain numeric values.")
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
# GENERATE REPORT SAFELY
# ---------------------------------------------------
try:
    report_text = generate_report(df, metrics)
except Exception as e:
    st.error(f"Report generation failed: {e}")
    st.stop()


# ---------------------------------------------------
# DOWNLOAD BUTTON (ALWAYS VISIBLE)
# ---------------------------------------------------
st.subheader("📥 Export Executive Report")

st.download_button(
    label="Download Executive Report",
    data=report_text,
    file_name="sales_report.txt",
    mime="text/plain"
)

st.markdown("---")


# ---------------------------------------------------
# MONTHLY TRENDS
# ---------------------------------------------------
st.subheader("📈 Monthly Performance Trends")

df['Year-Month'] = pd.to_datetime(df['Order Date']).dt.to_period('M')

monthly_revenue = df.groupby('Year-Month')['Total Revenue'].sum()
monthly_profit = df.groupby('Year-Month')['Total Profit'].sum()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Monthly Revenue")
    fig, ax = plt.subplots(figsize=(6, 3))
    monthly_revenue.plot(ax=ax)
    ax.set_ylabel("Revenue")
    ax.tick_params(axis='x', rotation=45)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    st.pyplot(fig, use_container_width=True)

with col2:
    st.markdown("### Monthly Profit")
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