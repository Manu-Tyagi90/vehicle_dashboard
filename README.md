# 🚗 Vehicle Registration Dashboard

🔗 **Live Dashboard:** [Vehicle Category Analysis](https://manu-tyagi90-vehicle-dashboard.streamlit.app/Vehicle_Category)

An interactive **data analytics dashboard** built with [Streamlit](https://streamlit.io/) to analyze and visualize **vehicle registration data** from the VAHAN portal.

The dashboard allows investors and analysts to:
- Explore **vehicle categories** (2W, 3W, 4W, etc.) over multiple years.
- Analyze **manufacturer-wise performance** across financial years.
- Calculate **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth.
- View **interactive charts** and download filtered datasets.
- Gain **quick investor insights** for decision making.

---

## 🛠 **Technologies Used**
- **Python 3.x**
- **Streamlit** (Frontend/UI Framework)
- **Pandas** (Data Handling)
- **Matplotlib / Seaborn** (Graphs/Charts)
- **streamlit-lottie** (Animations)
- **Requests** (Loading external Lottie animations)
- **Git** (Version Control)

---

## 📂 **Project Structure**
```
vehicle_dashboard/
│
├── app/
│   ├── streamlit_app.py          # Main homepage
│   └── pages/
│       ├── 1_Vehicle_Category.py
│       ├── 2_Manufacturer.py
│       ├── 3_Profile.py
│       └── 4_Insights.py
│
├── data/
│   ├── vehicle_category_registrations.csv
│   ├── manufacturer_2022-2023.csv
│   ├── manufacturer_2023-2024.csv
│   └── manufacturer_2024-2025.csv
│
└── README.md
```

---

## 🚀 **How to Run the Project Locally**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/vehicle-dashboard.git
cd vehicle-dashboard/app
```

### **2️⃣ Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
```

Activate venv:
- **Windows (CMD):**
```bash
venv\Scripts\activate
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install manually:
```bash
pip install streamlit pandas matplotlib seaborn requests streamlit-lottie
```

### **4️⃣ Prepare Your Data**
Place the CSV files:
- `vehicle_category_registrations.csv`
- `manufacturer_YEAR-YEAR.csv`
inside the `data/` folder.

---

### **5️⃣ Run the Application**
From the `app/` directory:
```bash
streamlit run streamlit_app.py
```

---

### **6️⃣ Use the Dashboard**
- The sidebar will let you switch between:
  - **Vehicle Category Analysis**
  - **Manufacturer Analysis**
  - **Profile**
  - **Investor Insights**
- Apply filters, view graphs, and download filtered datasets.

---

## 📸 **Screenshots**
<img width="1889" height="868" alt="image" src="https://github.com/user-attachments/assets/969a6e8b-f89e-4479-85b2-beb8074fd74c" />
<img width="1880" height="896" alt="image" src="https://github.com/user-attachments/assets/4869c764-0ae7-4de0-b5f0-69e0c7b006ca" />
<img width="1886" height="836" alt="image" src="https://github.com/user-attachments/assets/b6ebff53-aae6-4a07-be55-df25eba1f383" />
<img width="1889" height="912" alt="image" src="https://github.com/user-attachments/assets/d46d937b-5904-49d9-b6a1-30d98b51424e" />
<img width="1896" height="917" alt="image" src="https://github.com/user-attachments/assets/750c7ac8-c02e-4377-8e28-350aa55c6171" />

---

## 📌 **Future Improvements**
- Add monthly & quarterly trend visualizations.
- Integrate live VAHAN API (if possible).
- Include authentication for personalized dashboards.
- Export reports to PDF/Excel.

---

## 📄 **License**
This project is licensed under the MIT License - see the LICENSE file for details.
