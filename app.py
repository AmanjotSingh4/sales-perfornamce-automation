import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

from charts import (
    plot_monthly_trends,
    plot_sales_channel,
    plot_revenue_by_region
)

from kpis import (
    compute_kpis,
    generate_summary_text,
    generate_report_text
)

from summary import build_context, generate_ai_summary

plt.style.use("seaborn-v0_8-darkgrid")

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="logo.png",
    layout="wide"
)

# ------------------------------------------------
# HEADER
# ------------------------------------------------

col1, col2 = st.columns([1, 8], vertical_alignment="center")

with col1:
    st.image("logo.png", width=80)

with col2:
    st.markdown(
        "<h1 style='margin: 0;'>Sales Performance Dashboard</h1>",
        unsafe_allow_html=True
    )

st.markdown(
    "<p style='color:#9CA3AF;'>Upload a transactional sales dataset to generate automated performance insights.</p>",
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
    st.info("""
📁 Upload a transactional sales CSV file.

Required columns:
Region, 
Country, 
Item Type, 
Sales Channel,
Order Date, 
Ship Date, 
Units Sold,
Total Revenue, 
Total Cost, 
Total Profit
""")
    st.stop()

# ------------------------------------------------
# SAFE FILE READING
# ------------------------------------------------

try:
    file_bytes = uploaded_file.getvalue()
    df = pd.read_csv(io.BytesIO(file_bytes))
except Exception:
    st.error("❌ Failed to read the uploaded file.")
    st.stop()

df.columns = df.columns.str.strip()

# ------------------------------------------------
# BASIC VALIDATION
# ------------------------------------------------

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

missing = [col for col in required_columns if col not in df.columns]

if missing:
    st.error(f"❌ Missing required columns: {', '.join(missing)}")
    st.stop()

try:
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
except Exception:
    st.error("❌ Invalid date format.")
    st.stop()

numeric_cols = ["Units Sold", "Total Revenue", "Total Cost", "Total Profit"]

for col in numeric_cols:
    try:
        df[col] = pd.to_numeric(df[col])
    except Exception:
        st.error(f"❌ Column '{col}' must be numeric.")
        st.stop()

# ------------------------------------------------
# KPI SECTION
# ------------------------------------------------

kpis = compute_kpis(df)

st.subheader("📊 Executive Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${kpis['total_revenue']:,.2f}")
col2.metric("Total Profit", f"${kpis['total_profit']:,.2f}")
col3.metric("Average Profit per Order", f"${kpis['avg_profit']:,.2f}")

st.markdown(generate_summary_text(kpis))

# ------------------------------------------------
# DOWNLOAD REPORT
# ------------------------------------------------

report_text = generate_report_text(kpis)

st.download_button(
    "📄 Download Executive Report",
    report_text,
    "sales_report.txt"
)

# ------------------------------------------------
# AI SECTION
# ------------------------------------------------

context = build_context(kpis)

st.markdown("## 🤖 AI Strategic Summary")

if st.button("Generate AI Summary"):
    ai_summary = generate_ai_summary(context)
    st.markdown(ai_summary)

# Chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask about your sales data...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    full_prompt = context + f"\nUser Question: {user_input}"
    response = generate_ai_summary(full_prompt)
    st.session_state.chat_history.append(("assistant", response))

for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

# ------------------------------------------------
# CHARTS
# ------------------------------------------------

st.divider()

fig1, fig2 = plot_monthly_trends(df)
fig3 = plot_sales_channel(df)
fig4 = plot_revenue_by_region(df)

col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

st.pyplot(fig3)
st.pyplot(fig4)