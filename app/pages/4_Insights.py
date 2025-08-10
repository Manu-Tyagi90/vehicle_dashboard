import streamlit as st
import pandas as pd
import os

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/743/743007.png", width=80)
    st.markdown("## Vehicle Dashboard")
    st.markdown("---")
    st.markdown("**👤 Profile:**")
    st.write("Investor: [Your Name]")
    st.write("Email: your.email@example.com")
    st.markdown("---")
    st.markdown("### 📊 Navigation")
    st.write("Use the sidebar to switch pages.")
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

# --- Main Content ---
st.title("💡 Investor Insights")

# Load data
script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, '../../data')
category_file = os.path.join(data_folder, 'vehicle_category_registrations.csv')
category_df = pd.read_csv(category_file, skiprows=3, encoding='latin1')
category_df.columns = ['S No', 'Vehicle Category', '2025', '2024', '2023', '2022', 'TOTAL']
category_df = category_df.drop(columns=['S No'])
for col in ['2025', '2024', '2023', '2022', 'TOTAL']:
    category_df[col] = category_df[col].astype(str).str.replace(',', '').astype(int)
category_df['YoY_2024_vs_2023'] = ((category_df['2024'] - category_df['2023']) / category_df['2023'] * 100).round(2)
category_df['YoY_2023_vs_2022'] = ((category_df['2023'] - category_df['2022']) / category_df['2022'] * 100).round(2)

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
maker_pivot = maker_df.pivot(index='Maker', columns='Year', values='Registrations').reset_index()
maker_pivot['YoY_2023-2024_vs_2022-2023'] = (
    (maker_pivot['2023-2024'] - maker_pivot['2022-2023']) / maker_pivot['2022-2023'] * 100
).round(2)
maker_pivot['YoY_2024-2025_vs_2023-2024'] = (
    (maker_pivot['2024-2025'] - maker_pivot['2023-2024']) / maker_pivot['2023-2024'] * 100
).round(2)

# Top 5 Vehicle Categories by YoY Growth
st.subheader("🚀 Top 5 Vehicle Categories by YoY Growth (2024 vs 2023)")
top5_cat = category_df.sort_values('YoY_2024_vs_2023', ascending=False).head(5)
st.table(top5_cat[['Vehicle Category', 'YoY_2024_vs_2023']])

# Top 5 Manufacturers by YoY Growth
st.subheader("🚀 Top 5 Manufacturers by YoY Growth (2024-2025 vs 2023-2024)")
top5_maker = maker_pivot.sort_values('YoY_2024-2025_vs_2023-2024', ascending=False).head(5)
st.table(top5_maker[['Maker', 'YoY_2024-2025_vs_2023-2024']])

# Bottom 5 Manufacturers by YoY Growth
st.subheader("📉 Bottom 5 Manufacturers by YoY Growth (2024-2025 vs 2023-2024)")
bottom5_maker = maker_pivot.sort_values('YoY_2024-2025_vs_2023-2024', ascending=True).head(5)
st.table(bottom5_maker[['Maker', 'YoY_2024-2025_vs_2023-2024']])

st.info("These insights can help investors spot fast-growing or declining segments and companies.")