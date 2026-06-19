# Sales Performance Dashboard

An interactive Streamlit app for uploading a transactional sales CSV and exploring revenue, profit, and sales-channel performance.

## What It Does

- Validates uploaded sales data for the required business columns
- Computes executive KPIs such as total revenue, total profit, average profit, and top-performing region/item type
- Generates a text executive report for download
- Builds charts for monthly revenue and profit, revenue by sales channel, and revenue by region
- Produces an AI-generated strategic summary and chat responses from the uploaded dataset context

## Project Files

- `app.py`: Streamlit entry point and UI orchestration
- `charts.py`: Matplotlib visualizations
- `kpis.py`: KPI calculations and report text helpers
- `summary.py`: Context building and Groq-backed AI summary generation
- `analysis.py` and `report_generator.py`: Supporting metric/report utilities

## Requirements

Install the Python dependencies listed in `requirements.txt`:

- `streamlit`
- `pandas`
- `matplotlib`
- `openai`

The AI summary path also depends on a `grok_client` implementation available in the environment or project setup.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure the app assets and API integration expected by the code are available:
- `logo.png` in the repository root
- a working `grok_client.ask_groq` implementation for AI summaries

## Run

Start the dashboard with Streamlit:

```bash
streamlit run app.py
```

## Expected CSV Columns

The app expects these columns in the uploaded CSV:

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

## Usage Notes

- If the uploaded file is missing any required columns, the app stops with a validation error.
- `Order Date` and `Ship Date` must be parseable as dates.
- Numeric fields are coerced to numeric types before metrics and charts are generated.
