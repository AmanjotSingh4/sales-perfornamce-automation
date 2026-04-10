# Sales Performance Dashboard

Streamlit dashboard for analyzing transactional sales data. The app loads a CSV file, validates the expected columns, computes core KPIs, renders revenue and profit charts, and can generate both a downloadable executive report and an AI-assisted strategic summary.

## Features

- Upload a sales CSV and validate the required schema
- Compute total revenue, total profit, average profit per order, profit margin, and top-performing region/item type
- Visualize monthly revenue and profit trends, sales channel revenue, and revenue by region
- Download a text executive report from the computed KPIs
- Generate an AI summary using the context built from the sales metrics

## Requirements

- Python 3.10+
- `streamlit`
- `pandas`
- `matplotlib`
- `openai`

The AI summary flow in `summary.py` also expects a `grok_client` module with an `ask_groq` function available in the runtime environment.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure any required API credentials and helper modules for AI summaries are available in your environment.

## Run

Start the dashboard with Streamlit:

```bash
streamlit run app.py
```

## Usage

1. Open the app in your browser.
2. Upload a CSV with these required columns:

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

3. Review the KPI cards, charts, and written summary.
4. Download the executive report if needed.
5. Use the AI summary button or chat input after the dataset loads.

## Repository Notes

- `app.py` is the Streamlit entry point.
- `charts.py` contains the dashboard visualizations.
- `kpis.py` computes the dashboard metrics and report text.
- `summary.py` builds the AI context and submits prompts to the Groq helper.
- `report_generator.py` contains an additional formatted report helper.
