import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/eyowhite/Messy-dataset/main/warehouse_messy_data.csv"
print("Downloading dirty dataset...\n")

df = pd.read_csv(url)

print("--- First 5 Rows of the Dataset ---")
print(df.head())

print("\n--- Dataset Info (Look for the missing values here) ---")
print(df.info())

print("\n--- Starting Data Cleaning ---")

df.dropna(subset=['Product ID', 'Product Name'], inplace=True)

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')


df['Quantity'] = df['Quantity'].fillna(1)


df['Product Name'] = df['Product Name'].str.strip().str.title()


df.drop_duplicates(inplace=True)

print("Data Cleaning Complete. Missing values remaining:")
print(df.isnull().sum())


print("\n--- Generating Business Report ---")


df['Total_Revenue'] = df['Quantity'] * df['Price']

revenue_report = df.groupby('Product Name')['Total_Revenue'].sum().reset_index()
revenue_report = revenue_report.sort_values(by='Total_Revenue', ascending=False)

print("\nTotal Revenue by Product:")
print(revenue_report.to_string(index=False))

print("\n--- Exporting ---")
df.to_csv('clean_warehouse_data.csv', index=False)
print("SUCCESS: Clean data saved to 'clean_warehouse_data.csv'!")
