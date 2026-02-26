# 📊 Sales Performance Automation Dashboard

An interactive, product-oriented sales analytics tool built using **Streamlit** that allows non-technical users to upload transactional sales data and automatically generate executive insights, KPIs, visualizations, and downloadable reports.

This project demonstrates the transition from a simple data analysis script to a user-ready analytics product.

---

## 🚀 Project Overview

This dashboard enables users to:

- Upload their own CSV sales dataset
- Automatically validate and process the data
- Generate business-ready executive summaries
- Visualize revenue and profit trends
- Download an automated executive report

The goal is to combine **data processing, validation, business insight generation, and presentation** into a single usable tool.

---

## ✨ Key Features

### 📁 File Upload Capability
Users can upload their own sales dataset (CSV format).  
The app automatically processes the file.

### 🧹 Data Validation & Error Handling
The application validates:
- Required columns
- Date formats
- Numeric fields
- File encoding issues

User-friendly error messages are displayed instead of Python stack traces.

### 📊 Executive Summary
Displays:
- Total Revenue
- Total Profit
- Average Profit per Order
- Most Profitable Region
- Most Profitable Item Type

Designed in a business-friendly format.

### 📈 Visual Analytics
Includes:
- Monthly Revenue Trend
- Monthly Profit Trend
- Revenue by Sales Channel (Online vs Offline)
- Top 5 Countries by Revenue

### 📄 Downloadable Executive Report
Users can download a generated report summarizing key insights.

---

## 🖼 Dashboard Preview

![Dashboard Preview](dashboard_v2.png)

---

## 🗂 Project Structure
sales-performance-automation/
│
├── data/
│ └── sales.csv
│
├── output/
│ ├── cleaned_data.csv
│ └── report.txt
│
├── app.py
├── analysis.ipynb
├── requirements.txt
├── dashboard_v2.png
└── README.md


---

## 📂 Required Dataset Columns

The uploaded CSV must contain the following columns:

- Region
- Country
- Item Type
- Sales Channel
- Order Date
- Total Revenue
- Total Profit

If required columns are missing, the app will display a clear validation message.

---

## 🛠 Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib

---

## 🎯 Business Objective

This project was designed to shift from:

> "Code that analyzes data"

To:

> "A usable analytics product for non-technical stakeholders."

It emphasizes:
- Clean architecture
- Separation of preprocessing and presentation layers
- User validation and error handling
- Executive-ready reporting

---

## 🔮 Future Improvements

- Add sales forecasting module
- Deploy publicly via Streamlit Cloud
- Add user-controlled filters
- Replace Matplotlib with interactive Plotly charts
- Add downloadable PDF executive report
- Add multi-file comparison capability

---

## 📌 How to Run Locally

1. Clone the repository:
git clone


2. Navigate into the folder:


cd sales-performance-automation


3. Install dependencies:


pip install -r requirements.txt


4. Run the app:


streamlit run app.py


---

## 💼 Portfolio Note

This project demonstrates:

- Data cleaning & preprocessing
- KPI computation
- Business insight generation
- Validation & robust error handling
- Dashboard development
- Product-oriented thinking

It is structured as a portfolio-ready analytics product.

---