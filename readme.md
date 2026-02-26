# 📊 Sales Performance Analytics Dashboard

## 📌 Project Overview

This project analyzes global transactional sales data to generate structured business insights, key performance indicators (KPIs), and an interactive executive dashboard.

The goal was to transform raw CSV sales data into actionable intelligence suitable for business stakeholders.

The project includes:

- Data cleaning and preprocessing
- KPI computation
- Business insight generation
- Automated executive report creation
- Interactive Streamlit dashboard

---

## 🖼 Dashboard Preview

![Dashboard Preview](dashboard_preview.png)

> *Interactive dashboard built using Streamlit displaying KPIs, trends, and profitability insights.*

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

The dataset contains mixed categorical, numerical, and time-series data.

---

## ⚙️ Data Processing & Cleaning

The following preprocessing steps were performed:

- Loaded CSV using pandas
- Inspected dataset using `.head()` and `.info()`
- Converted `Order Date` and `Ship Date` to datetime
- Ensured numeric columns were properly typed
- Handled missing values
- Removed duplicate rows
- Saved cleaned dataset as `cleaned_data.csv`

---

## 📈 Key Business Insights Generated

The system automatically computes:

- Total Revenue
- Total Profit
- Average Profit per Order
- Most Profitable Region
- Most Profitable Item Type
- Revenue by Sales Channel
- Top 5 Countries by Revenue
- Monthly Revenue Trend
- Monthly Profit Trend
- Profit Margin

Insights are exported automatically into a formatted `report.txt`.

---

## 📊 Interactive Dashboard Features

The Streamlit dashboard includes:

- KPI metric cards
- Monthly revenue & profit trends
- Revenue by sales channel
- Top 5 countries by revenue
- Profitability insights
- Sidebar filters (Region, Sales Channel)

To run locally:

```bash
python -m streamlit run app.py