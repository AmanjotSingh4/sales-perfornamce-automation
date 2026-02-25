# 📊 Sales Performance Analytics Dashboard

## 📌 Project Overview

This project analyzes global transactional sales data to generate business insights, key performance indicators (KPIs), and an interactive executive dashboard.

The objective was to transform raw CSV sales data into structured, actionable intelligence suitable for business decision-making.

The project includes:

- Data cleaning and preprocessing
- KPI computation
- Business insight generation
- Automated executive report creation
- Interactive Streamlit dashboard for stakeholders

---

## 🗂 Dataset Description

The dataset contains transactional sales records including:

- Region
- Country
- Item Type
- Sales Channel (Online / Offline)
- Order Date & Ship Date
- Units Sold
- Unit Price & Unit Cost
- Total Revenue
- Total Cost
- Total Profit

The data includes mixed categorical, numerical, and time-series features.

---

## ⚙️ Data Processing & Cleaning

The following preprocessing steps were performed:

- Loaded CSV using pandas
- Inspected dataset using `.head()` and `.info()`
- Converted `Order Date` and `Ship Date` to datetime format
- Ensured numeric columns were properly typed
- Handled missing values
- Removed duplicate records
- Saved cleaned dataset as `cleaned_data.csv`

---

## 📈 Key Business Insights Generated

The system automatically computes:

- ✅ Total Revenue
- ✅ Total Profit
- ✅ Average Profit per Order
- ✅ Most Profitable Region
- ✅ Most Profitable Item Type
- ✅ Revenue by Sales Channel
- ✅ Top 5 Countries by Revenue
- ✅ Monthly Revenue Trend
- ✅ Monthly Profit Trend
- ✅ Profit Margin

### Example Insight

- Offline sales generated significantly more revenue than online sales.
- Cosmetics emerged as the most profitable product category.
- Certain regions consistently outperform others in profitability.

All insights are automatically exported to a formatted `report.txt`.

---

## 📊 Interactive Dashboard (Streamlit)

A professional interactive dashboard was built using Streamlit.

### Dashboard Features:

- KPI metrics display
- Monthly revenue & profit trends
- Revenue by sales channel
- Top 5 countries by revenue
- Profitability insights
- Sidebar filters for:
  - Region
  - Sales Channel

The dashboard provides a stakeholder-friendly interface and does not expose code.

To run locally:

```bash
python -m streamlit run app.py