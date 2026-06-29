import pandas as pd
import numpy as np

# 1. Fetching the messy dataset directly from a raw GitHub repository
url = "https://raw.githubusercontent.com/eyowhite/Messy-dataset/main/warehouse_messy_data.csv"
print("Downloading dirty dataset...\n")

# Load the data into a Pandas DataFrame
df = pd.read_csv(url)

# 2. Inspecting the damage
print("--- First 5 Rows of the Dataset ---")
print(df.head())

print("\n--- Dataset Info (Look for the missing values here) ---")
print(df.info())

# 3. Cleaning the Data
print("\n--- Starting Data Cleaning ---")

# A. Drop rows where 'Product ID' or 'Product Name' is missing (Updated column names)
df.dropna(subset=['Product ID', 'Product Name'], inplace=True)

# B. Force the 'Quantity' column to be numbers. 
# (If you look at Row 1, someone typed "two hundred" instead of 200. This forces text to turn into blanks so we can fix them).
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# C. Fill missing 'Quantity' values with 1
df['Quantity'] = df['Quantity'].fillna(1)

# D. Clean the 'Product Name' text (Updated column name)
df['Product Name'] = df['Product Name'].str.strip().str.title()

# E. Remove any exact duplicate rows
df.drop_duplicates(inplace=True)

print("Data Cleaning Complete. Missing values remaining:")
print(df.isnull().sum())

# 4. Aggregation (Calculating Business Metrics)
print("\n--- Generating Business Report ---")

# Calculate Total Revenue
df['Total_Revenue'] = df['Quantity'] * df['Price']

# Group by 'Product Name' (Updated column name)
revenue_report = df.groupby('Product Name')['Total_Revenue'].sum().reset_index()
revenue_report = revenue_report.sort_values(by='Total_Revenue', ascending=False)

print("\nTotal Revenue by Product:")
print(revenue_report.to_string(index=False))

# 5. Export
print("\n--- Exporting ---")
df.to_csv('clean_warehouse_data.csv', index=False)
print("SUCCESS: Clean data saved to 'clean_warehouse_data.csv'!")