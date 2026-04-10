# Sales Performance Automation

Streamlit dashboard for analyzing transactional sales data and generating automated business insights.

## What it does

- Upload a sales CSV file and validate the required columns
- Calculate core KPIs such as total revenue, total profit, average profit, and profit margin
- Visualize monthly revenue and profit trends
- Compare revenue by sales channel and region
- Generate a short executive summary and report text
- Optionally call Groq-powered AI summarization through the configured client

## Project Structure

- `app.py` - Streamlit entry point and dashboard UI
- `charts.py` - Matplotlib chart helpers
- `kpis.py` - KPI calculations and formatted insight text
- `summary.py` - Context building and AI summary generation
- `analysis.py` - Additional metric helper used by the project
- `preprocess.py` - Basic data cleaning helpers
- `report_generator.py` - Text report generation
- `grok_client.py` - Groq/OpenAI-compatible client wrapper

## Requirements

- Python 3.10+
- Streamlit
- Pandas
- Matplotlib
- OpenAI Python SDK

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API key if you want AI summaries:

```bash
export GROQ_API_KEY="your_api_key_here"
```

## Run the app

```bash
streamlit run app.py
```

## Data Format

The dashboard expects a CSV file with these columns:

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

## Notes

- The app uses `logo.png` for the page icon and header image.
- Dates are parsed from the uploaded CSV before charts and summaries are generated.
- If the AI service is unavailable or the API key is missing, the app can still be used for local analysis.
