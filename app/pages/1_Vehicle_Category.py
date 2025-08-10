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

# ✅ Working car animation
lottie_car = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")

# ---------------- Page Content ----------------
st.title("🚗 Vehicle Category Analysis")

# Show animation safely
if lottie_car:
    st_lottie(lottie_car, height=200, key="car-category")
else:
    st.warning("⚠️ Animation could not be loaded. Try with another Lottie URL.")

# ---------------- Load Data ----------------
script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, '../../data')
category_file = os.path.join(data_folder, 'vehicle_category_registrations.csv')
category_df = pd.read_csv(category_file, skiprows=3, encoding='latin1')
category_df.columns = ['S No', 'Vehicle Category', '2025', '2024', '2023', '2022', 'TOTAL']
category_df = category_df.drop(columns=['S No'])

# Clean Data
for col in ['2025', '2024', '2023', '2022', 'TOTAL']:
    category_df[col] = category_df[col].astype(str).str.replace(',', '').astype(int)

# Calculate YoY Growth
category_df['YoY_2024_vs_2023'] = ((category_df['2024'] - category_df['2023']) / category_df['2023'] * 100).round(2)
category_df['YoY_2023_vs_2022'] = ((category_df['2023'] - category_df['2022']) / category_df['2022'] * 100).round(2)

# ---------------- Filters ----------------
st.markdown("### 🔍 Filter Vehicle Categories")
category_options = category_df['Vehicle Category'].unique().tolist()
selected_categories = st.multiselect("Select Categories:", category_options, default=category_options[:5])
filtered_df = category_df[category_df['Vehicle Category'].isin(selected_categories)]

# ---------------- Data Table ----------------
st.subheader("📄 Data Table")
st.dataframe(filtered_df[['Vehicle Category', '2022', '2023', '2024', 'YoY_2023_vs_2022', 'YoY_2024_vs_2023']])

# ---------------- Bar Chart ----------------
st.subheader("📊 YoY Growth (2024 vs 2023)")
fig, ax = plt.subplots()
ax.bar(filtered_df['Vehicle Category'], filtered_df['YoY_2024_vs_2023'], color='#1f77b4')
plt.xticks(rotation=90)
plt.ylabel("YoY Growth (%)")
plt.xlabel("Vehicle Category")
st.pyplot(fig)

# ---------------- Line Chart ----------------
st.subheader("📈 Registrations Trend")
if not filtered_df.empty:
    st.line_chart(filtered_df.set_index('Vehicle Category')[['2022', '2023', '2024']].T)

# ---------------- Investor Insight ----------------
st.subheader("💡 Quick Insight")
top_growth = filtered_df.sort_values('YoY_2024_vs_2023', ascending=False).head(1)
if not top_growth.empty:
    st.success(f"Top Growth Category: **{top_growth.iloc[0]['Vehicle Category']}** with **{top_growth.iloc[0]['YoY_2024_vs_2023']}%** growth from 2023 to 2024.")
