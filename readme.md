# 📊 AI-Powered Sales Performance Dashboard

A production-ready analytics application built with **Streamlit**, combining structured KPI computation, automated validation, interactive visualizations, and AI-generated executive insights.

This project demonstrates the evolution from a basic data analysis script into a modular, deployable, AI-enhanced business intelligence product.

---

## 🌐 Live Application

🚀 **Streamlit Deployment:**  
(Add your Streamlit Community Cloud link here)

---

## 🚀 Project Overview

This dashboard allows non-technical users to:

- Upload transactional sales data
- Automatically validate dataset structure
- Generate executive-level KPI summaries
- Visualize revenue and profit trends
- Interact with AI for strategic analysis
- Download a structured executive summary report

The architecture separates analytics logic, visualization, AI processing, and UI layers for clean, scalable engineering.

---

## ✨ Core Features

### 📁 CSV File Upload
Users can upload their own transactional sales dataset in CSV format.

---

### 🧹 Robust Data Validation

The system performs:

- Required column validation
- Case-insensitive schema checking
- Date format validation
- Numeric field validation
- Safe in-memory file handling

All errors are handled gracefully with user-friendly messages.

---

### 📊 Executive KPI Engine

Automatically computes:

- Total Revenue
- Total Profit
- Average Profit per Order
- Profit Margin
- Most Profitable Region
- Most Profitable Item Type
- Revenue by Sales Channel

KPI logic is centralized in `kpis.py` to ensure a **single source of truth** across:

- UI display
- AI context generation
- Downloadable reports

---

### 🤖 AI Strategic Summary (Groq Integration)

Integrated with Groq API (OpenAI-compatible interface):

- Generates executive-level summaries
- Provides strategic insights
- Allows user Q&A via chat interface
- Context-aware responses based on computed KPIs

The AI layer consumes structured KPI output for consistent analysis.

---

### 💬 Interactive AI Chat

Users can:

- Ask strategic questions about the dataset
- Explore performance drivers
- Request business-level explanations

Chat history is session-managed for conversational continuity.

---

### 📈 Visual Analytics

Includes modular chart generation:

- Monthly Revenue Trend
- Monthly Profit Trend
- Revenue by Sales Channel
- Revenue by Region

All visualization logic is separated into `charts.py` for maintainability.

---

### 📄 Downloadable Executive Report

Generates a structured executive summary as a `.txt` report based on centralized KPI logic.

This ensures consistency between:
- On-screen metrics
- AI analysis
- Downloaded report

---

### 🎨 Branded Product UI

- Custom logo
- Dark-themed professional layout
- Clean executive-style hierarchy
- Wide layout configuration
- Structured section separation

---

## 📂 Required Dataset Structure

Uploaded CSV must include:

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

Validation is case-insensitive, but required fields must exist.

---

## 🗂 Project Structure
sales-performance-dashboard/
    │
    ├── app.py # Main Streamlit application
    ├── kpis.py # KPI computation + summary/report logic
    ├── charts.py # Modular visualization functions
    ├── summary.py # AI context + Groq integration
    ├── logo.png # Branding asset
    ├── requirements.txt
    ├── README.md
    └── .streamlit/
    └── config.toml # Theme configuration


---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Groq API (OpenAI-compatible endpoint)
- Modular application architecture

---

## 🧠 Engineering Highlights

- Separation of concerns (UI, analytics, AI, visualization)
- Centralized KPI engine (single source of truth)
- Safe in-memory file ingestion
- Structured schema validation
- Session-managed AI chat
- Modular chart rendering
- Clean Git workflow
- Cloud deployment via Streamlit Community Cloud

---

## 🔮 Planned Enhancements

- Executive-grade PDF report export
- Interactive filters (date range, region, channel)
- Forecasting module (time-series projection)
- Plotly-based interactive charts
- Multi-dataset comparison
- Role-based access control

---

## ▶️ Run Locally

1️⃣ Clone the repository:
git clone https://github.com/YOUR_USERNAME/sales-performance-dashboard.git


2️⃣ Navigate into the project folder:


cd sales-performance-dashboard


3️⃣ Install dependencies:


pip install -r requirements.txt


4️⃣ Set your Groq API key (environment variable):

Windows:

set GROQ_API_KEY=your_key_here


macOS / Linux:

export GROQ_API_KEY=your_key_here


5️⃣ Run the application:


streamlit run app.py


---

## 🔐 API Key Handling

The application uses environment variables for API security.

Do **not** hardcode API keys inside source files.

For Streamlit Community Cloud deployment:
- Add `GROQ_API_KEY` inside **App Settings → Secrets**

---

## 💼 Portfolio Positioning

This project demonstrates:

- Transition from analysis script to deployable product
- Modular backend logic design
- Business KPI abstraction
- AI integration into analytics workflows
- Clean UI/UX hierarchy
- Production-oriented engineering thinking

It reflects a shift from pure data analysis toward AI-enabled product development.