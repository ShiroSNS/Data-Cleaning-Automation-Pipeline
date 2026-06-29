# Automated Data Cleaning & Reporting Pipeline 🧹📊

An automated Python script designed to ingest raw, unstructured warehouse data, perform systematic data cleaning, and output business-ready financial metrics.

## 🚀 Business Value
Startups and e-commerce companies often deal with messy, human-entered data. This script eliminates manual spreadsheet formatting by automatically handling null values, standardizing data types, removing duplicates, and aggregating revenue metrics using vectorization.

## 🛠️ Tech Stack
- **Language:** Python
- **Data Processing Engine:** Pandas, NumPy

## 📋 Core Features
- **Data Ingestion:** Fetches raw CSV data programmatically.
- **Automated Scrubbing:** Drops unrecoverable rows, imputes missing quantities, and strips/formats text strings (Title Case).
- **Type Casting:** Forces unstructured text into calculable numeric formats.
- **Aggregation:** Calculates total revenue per product category and outputs a sorted terminal report.
- **Export:** Automatically generates a pristine `clean_warehouse_data.csv` ready for dashboard integration.

## 📦 How to Run
1. Clone the repository:

  https://github.com/ShiroSNS/Data-Cleaning-Automation-Pipeline

3. Install dependencies:
   ```bash
   pip install pandas numpy

4. Execute the pipeline:
    ```bash
   python cleaner.py
