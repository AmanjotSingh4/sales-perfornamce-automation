import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
plt.style.use("seaborn-v0_8-darkgrid")
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="logo.png",
    layout="wide"
)

col1, col2 = st.columns([1, 8], vertical_alignment="center")

with col1:
    st.image("logo.png", width=80)

with col2:
    st.markdown(
        "<h1 style='margin: 0;'>Sales Performance Dashboard</h1>",
        unsafe_allow_html=True
    )

st.markdown(
    "<p style='color:#9CA3AF; margin-top: 5px;'>Upload a transactional sales dataset to generate automated performance insights.</p>",
    unsafe_allow_html=True
)
# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your sales CSV file",
    type=["csv"]
)

if uploaded_file is None:
    st.info(
    """
📁 **Upload a transactional sales CSV file to begin analysis.**

Your dataset must include the following required columns:

- Region  
- Country  
- Item Type  
- Sales Channel  
- Order Date  
- Ship Date  
- Units Sold  
- Total Revenue  
- Total Cost  
- Total Profit  

Make sure:
- The file is in CSV format  
- Column names are spelled correctly  
- Dates are in a valid format (e.g., YYYY-MM-DD)
"""
)
    st.stop()

# ----------------------------------------
# SAFE FILE READING
# ----------------------------------------
try:
    file_bytes = uploaded_file.getvalue()
    df = pd.read_csv(io.BytesIO(file_bytes))
except Exception:
    st.error("❌ Failed to read the uploaded file. Please upload a valid CSV file.")
    st.stop()

# ----------------------------------------
# CLEAN COLUMN NAMES
# ----------------------------------------
df.columns = df.columns.str.strip()

# ----------------------------------------
# REQUIRED COLUMN VALIDATION (Case-insensitive)
# ----------------------------------------
required_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Date",
    "Ship Date",
    "Units Sold",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

df_columns_lower = [col.lower() for col in df.columns]
required_lower = [col.lower() for col in required_columns]

missing_columns = [
    required_columns[i]
    for i, col in enumerate(required_lower)
    if col not in df_columns_lower
]

if missing_columns:
    st.error(
        f"""
❌ The uploaded file is missing required columns:

{', '.join(missing_columns)}

Please upload a valid transactional sales dataset.
"""
    )
    st.stop()

# ----------------------------------------
# DATE VALIDATION
# ----------------------------------------
try:
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
except Exception:
    st.error("❌ 'Order Date' and 'Ship Date' must contain valid date values.")
    st.stop()

# ----------------------------------------
# NUMERIC VALIDATION (Robust Conversion)
# ----------------------------------------
numeric_cols = [
    "Units Sold",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

for col in numeric_cols:
    try:
        df[col] = pd.to_numeric(df[col])
    except Exception:
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

with st.container():
    st.markdown("### 🏆 Key Insights")
    st.info(f"""
    • Most Profitable Region: **{most_profitable_region}**
    • Most Profitable Item Type: **{most_profitable_item}**
    • Profit Margin: **{profit_margin:.2f}%**
    """)

# ------------------------------------------------
# MONTHLY TRENDS
# ------------------------------------------------

df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_revenue = df.groupby("Year-Month")["Total Revenue"].sum()
monthly_profit = df.groupby("Year-Month")["Total Profit"].sum()

# st.subheader("📈 Monthly Revenue")

fig1, ax1 = plt.subplots(figsize=(6,4))
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
monthly_revenue.plot(ax=ax1, color="#4CAF50", linewidth=2)
ax1.set_ylabel("Revenue")
# st.pyplot(fig1)

# st.subheader("📉 Monthly Profit")

fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
monthly_profit.plot(ax=ax2, color="#FF6B6B", linewidth=2)
ax2.set_ylabel("Profit")
# st.pyplot(fig2)

# ------------------------------------------------
# REVENUE BY SALES CHANNEL
# ------------------------------------------------

# st.subheader("🛒 Revenue by Sales Channel")

fig3, ax3 = plt.subplots(figsize=(6,4))
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
sales_channel_revenue.plot(
    kind="bar",
    ax=ax3,
    color=["#4CAF50", "#2196F3"]
)
ax3.set_ylabel("Total Revenue")
# st.pyplot(fig3)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Revenue")
    st.pyplot(fig1)

with col2:
    st.subheader("📉 Monthly Profit")
    st.pyplot(fig2)
st.subheader("🛒 Revenue by Sales Channel")
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