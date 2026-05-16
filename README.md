# Sales Performance Automation

An interactive Streamlit dashboard for analyzing transactional sales data. The app loads a CSV file, validates the expected schema, computes core KPIs, renders revenue and profit charts, and can generate AI-assisted strategic summaries.

## Features

- Upload a sales CSV and inspect the results in a dashboard
- Compute total revenue, total profit, average profit, and profit margin
- Identify the most profitable region and item type
- Visualize monthly trends, sales channel revenue, and regional revenue
- Download a text-based executive report
- Generate an AI summary from the computed sales context

## Requirements

The input CSV must include these columns:

- `Region`
- `Country`
- `Item Type`
- `Sales Channel`
- `Order Date`
- `Ship Date`
- `Units Sold`
- `Total Revenue`
- `Total Cost`
- `Total Profit`

## Project Structure

- `app.py` - Streamlit entry point and UI
- `charts.py` - Matplotlib chart helpers
- `kpis.py` - KPI calculations and report text helpers
- `summary.py` - AI summary context and generation
- `analysis.py` - Basic metric calculations
- `preprocess.py` - Data cleaning utilities
- `report_generator.py` - Report generation helpers
- `grok_client.py` - AI client integration

## Local Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Streamlit app:

```bash
streamlit run app.py
```

## How To Use

1. Open the app in your browser after starting Streamlit.
2. Upload a CSV that matches the required schema.
3. Review the KPI cards, AI summary, and charts.
4. Use the download button to export the executive report.

## Notes

- Dates are parsed from the `Order Date` and `Ship Date` columns.
- Numeric fields are validated before the charts and KPIs are generated.
- The app expects a `logo.png` file in the repository root for branding in the UI.
