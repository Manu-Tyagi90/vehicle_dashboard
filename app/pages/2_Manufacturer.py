import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests

# ---------------- Sidebar ----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/743/743007.png", width=80)
    st.markdown("## Vehicle Dashboard")
    st.markdown("---")
    st.markdown("**👤 Profile:**")
    st.write("Investor: Your Name")
    st.write("Email: your.email@example.com")
    st.markdown("---")
    st.markdown("### 📊 Navigation")
    st.write("Use the sidebar to switch between pages.")
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

# ---------------- Lottie Animation Loader ----------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ✅ Working factory animation
lottie_factory = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_touohxv0.json")

# Show animation safely
if lottie_factory:
    st_lottie(lottie_factory, height=200, key="factory-animation")
else:
    st.warning("⚠️ Animation could not be loaded. Try with another Lottie URL.")

# ---------------- Page Title ----------------
st.title("🏭 Manufacturer Analysis")

# ---------------- Load Manufacturer Data ----------------
script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, '../../data')
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

# Pivot for analysis
maker_pivot = maker_df.pivot(index='Maker', columns='Year', values='Registrations').reset_index()
maker_pivot['YoY_2023-2024_vs_2022-2023'] = ((maker_pivot['2023-2024'] - maker_pivot['2022-2023']) / maker_pivot['2022-2023'] * 100).round(2)
maker_pivot['YoY_2024-2025_vs_2023-2024'] = ((maker_pivot['2024-2025'] - maker_pivot['2023-2024']) / maker_pivot['2023-2024'] * 100).round(2)

# ---------------- Filters ----------------
st.markdown("### 🔍 Filter Manufacturers")
maker_options = maker_pivot['Maker'].unique().tolist()
selected_makers = st.multiselect("Select Manufacturer(s):", maker_options, default=maker_options[:8])
filtered_maker_df = maker_pivot[maker_pivot['Maker'].isin(selected_makers)]

# ---------------- Data Table ----------------
st.subheader("📄 Manufacturer Data Table")
st.dataframe(filtered_maker_df[['Maker', '2022-2023', '2023-2024', '2024-2025', 'YoY_2023-2024_vs_2022-2023', 'YoY_2024-2025_vs_2023-2024']])

# ---------------- Bar Chart ----------------
st.subheader("📊 YoY Growth (2024-2025 vs 2023-2024)")
fig, ax = plt.subplots()
ax.bar(filtered_maker_df['Maker'], filtered_maker_df['YoY_2024-2025_vs_2023-2024'], color='#ff7f0e')
plt.xticks(rotation=90)
plt.ylabel("YoY Growth (%)")
plt.xlabel("Manufacturer")
st.pyplot(fig)

# ---------------- Investor Insight ----------------
st.subheader("🎯 Top-Up Achievement")
top_growth = filtered_maker_df.sort_values('YoY_2024-2025_vs_2023-2024', ascending=False).head(1)
if not top_growth.empty:
    top_maker = top_growth.iloc[0]['Maker']
    top_percent = top_growth.iloc[0]['YoY_2024-2025_vs_2023-2024']
st.markdown(f"""
<div style='background-color:#fff8e1; padding:20px; border-radius:10px; border-left:6px solid #fbc02d'>
    <h3 style='color:#333; text-shadow: 1px 1px 2px #ccc;'>🏆 Top Growth Manufacturer</h3>
    <p style='color:#444; font-size:16px; text-shadow: 0.5px 0.5px 1px #aaa;'>
        <strong>{top_maker}</strong> achieved a phenomenal 
        <span style='color:#f57c00; font-weight:bold;'>{top_percent}%</span> growth in registrations 
        from <strong>2023-2024</strong> to <strong>2024-2025</strong>.
    </p>
</div>
""", unsafe_allow_html=True)

