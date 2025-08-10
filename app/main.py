import pandas as pd
import os

# --- Setup paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, '../data')

# --- 1. Load and clean Vehicle Category-wise Data ---
category_file = os.path.join(data_folder, 'vehicle_category_registrations.csv')
category_df = pd.read_csv(category_file, skiprows=3, encoding='latin1')
category_df.columns = ['S No', 'Vehicle Category', '2025', '2024', '2023', '2022', 'TOTAL']
category_df = category_df.drop(columns=['S No'])

# Remove commas and convert to int
for col in ['2025', '2024', '2023', '2022', 'TOTAL']:
    category_df[col] = category_df[col].astype(str).str.replace(',', '').astype(int)

# Calculate YoY growth
category_df['YoY_2024_vs_2023'] = ((category_df['2024'] - category_df['2023']) / category_df['2023'] * 100).round(2)
category_df['YoY_2023_vs_2022'] = ((category_df['2023'] - category_df['2022']) / category_df['2022'] * 100).round(2)

print("Vehicle Category YoY Growth:")
print(category_df[['Vehicle Category', '2022', '2023', '2024', 'YoY_2023_vs_2022', 'YoY_2024_vs_2023']].head())

# --- 2. Load and combine Manufacturer-wise Data from multiple files ---
years = ['2022-2023', '2023-2024', '2024-2025']
maker_files = [os.path.join(data_folder, f'manufacturer_{year}.csv') for year in years]
maker_dfs = []

for file, year in zip(maker_files, years):
    df = pd.read_csv(file, skiprows=3, encoding='latin1')
    df.columns = ['S No', 'Maker', 'Registrations', 'TOTAL']
    df = df[['Maker', 'Registrations']]
    df['Year'] = year
    df['Registrations'] = df['Registrations'].astype(str).str.replace(',', '').astype(int)
    maker_dfs.append(df)

maker_df = pd.concat(maker_dfs, ignore_index=True)

# Pivot for YoY calculation
maker_pivot = maker_df.pivot(index='Maker', columns='Year', values='Registrations').reset_index()

# Calculate YoY growth for manufacturers
maker_pivot['YoY_2023-2024_vs_2022-2023'] = (
    (maker_pivot['2023-2024'] - maker_pivot['2022-2023']) / maker_pivot['2022-2023'] * 100
).round(2)
maker_pivot['YoY_2024-2025_vs_2023-2024'] = (
    (maker_pivot['2024-2025'] - maker_pivot['2023-2024']) / maker_pivot['2023-2024'] * 100
).round(2)

print("\nManufacturer YoY Growth:")
print(maker_pivot[['Maker', '2022-2023', '2023-2024', '2024-2025', 'YoY_2023-2024_vs_2022-2023', 'YoY_2024-2025_vs_2023-2024']].head())