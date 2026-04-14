# Sales Performance Automation

A lightweight, data‑driven dashboard built with **Streamlit** that automates the analysis of sales data, visualises key metrics, and helps sales teams make data‑backed decisions faster.

> **Repository**: `AmanjotSingh4/sales-perfornamce-automation`  
> **Author**: Amanjot Singh  
> **Last updated**: 2026‑04‑14  

> ⚠️ *The repository name contains a typo (`perfornamce`). The code works as‑is, but the README refers to the intended “performance” spelling.*

---

## Overview

- **Purpose** – Quickly ingest raw sales data, compute KPIs, and present them in an interactive web UI.
- **Key Features**
  - Automatic data ingestion from CSV/Excel files.
  - KPI calculations (revenue, units sold, conversion rate, etc.).
  - Trend & forecast visualisations (line charts, bar charts, heatmaps).
  - Customisable filters (date range, region, product line).
  - Exportable reports (PDF/CSV).
- **Tech Stack**
  - Python 3.10+
  - Streamlit 1.30+
  - Pandas, NumPy, Plotly
  - Optional: `openpyxl` for Excel support

---

## Setup

> **Prerequisites**  
> - Python 3.10+ (recommended via `pyenv` or `conda`)  
> - `pip` (Python package manager)

### 1. Clone the repo

```bash
git clone https://github.com/AmanjotSingh4/sales-perfornamce-automation.git
cd sales-perfornamce-automation
```

### 2. Create a virtual environment

```bash
# Using venv
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

> The project ships with a minimal `requirements.txt`. If it’s missing, create one with the following content:

```text
streamlit>=1.30
pandas>=2.0
numpy>=1.26
plotly>=5.18
openpyxl>=3.

## Usage
Use the project workflows to run, validate, and iterate safely.
- Example: `streamlit run app.py`.

## Architecture
Core modules handle ingestion, analysis, remediation, and notifications.

## Troubleshooting
- Validate environment variables and dependencies.

## Contribution
- Open focused pull requests with clear descriptions.
