import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Performance Dashboard")
st.markdown("Upload a transactional sales dataset to generate automated performance insights.")

# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your sales CSV file",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Please upload a CSV file to begin analysis.")
    st.stop()

# ------------------------------------------------
# SAFE FILE READING (NO POINTER ISSUES)
# ------------------------------------------------

try:
    file_bytes = uploaded_file.getvalue()
    df = pd.read_csv(io.BytesIO(file_bytes))
except Exception:
    st.error("❌ Failed to read the uploaded file. Please upload a valid CSV file.")
    st.stop()

# Clean column names
df.columns = df.columns.str.strip()

# ------------------------------------------------
# VALIDATION
# ------------------------------------------------

required_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Date",
    "Total Revenue",
    "Total Profit"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"❌ Missing required columns: {', '.join(missing_columns)}")
    st.stop()

# Convert date safely
try:
    df["Order Date"] = pd.to_datetime(df["Order Date"])
except Exception:
    st.error("❌ 'Order Date' must contain valid date values.")
    st.stop()

# Ensure numeric columns
numeric_cols = ["Total Revenue", "Total Profit"]

for col in numeric_cols:
    if not pd.api.types.is_numeric_dtype(df[col]):
        st.error(f"❌ Column '{col}' must contain numeric values.")
        st.stop()

# ------------------------------------------------
# KPI CALCULATIONS
# ------------------------------------------------

total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()
avg_profit = df["Total Profit"].mean()

profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

most_profitable_region = df.groupby("Region")["Total Profit"].sum().idxmax()
most_profitable_item = df.groupby("Item Type")["Total Profit"].sum().idxmax()

sales_channel_revenue = df.groupby("Sales Channel")["Total Revenue"].sum()

# ------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------

st.subheader("📊 Executive Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Average Profit per Order", f"${avg_profit:,.2f}")

st.success(
    f"""
Most Profitable Region: {most_profitable_region}  
Most Profitable Item Type: {most_profitable_item}  
Overall Profit Margin: {profit_margin:.2f}%
"""
)

# ------------------------------------------------
# MONTHLY TRENDS
# ------------------------------------------------

df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_revenue = df.groupby("Year-Month")["Total Revenue"].sum()
monthly_profit = df.groupby("Year-Month")["Total Profit"].sum()

st.subheader("📈 Monthly Revenue")

fig1, ax1 = plt.subplots()
monthly_revenue.plot(ax=ax1)
ax1.set_ylabel("Revenue")
st.pyplot(fig1)

st.subheader("📉 Monthly Profit")

fig2, ax2 = plt.subplots()
monthly_profit.plot(ax=ax2)
ax2.set_ylabel("Profit")
st.pyplot(fig2)

# ------------------------------------------------
# REVENUE BY SALES CHANNEL
# ------------------------------------------------

st.subheader("🛒 Revenue by Sales Channel")

fig3, ax3 = plt.subplots()
sales_channel_revenue.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Total Revenue")
st.pyplot(fig3)

# ------------------------------------------------
# DOWNLOAD REPORT
# ------------------------------------------------

report_text = f"""
SALES PERFORMANCE REPORT
------------------------
Total Revenue: ${total_revenue:,.2f}
Total Profit: ${total_profit:,.2f}
Average Profit per Order: ${avg_profit:,.2f}

Most Profitable Region: {most_profitable_region}
Most Profitable Item Type: {most_profitable_item}

Overall Profit Margin: {profit_margin:.2f}%
"""

st.download_button(
    label="📄 Download Executive Report",
    data=report_text,
    file_name="sales_report.txt",
    mime="text/plain"
)