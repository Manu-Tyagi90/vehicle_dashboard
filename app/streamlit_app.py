import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/743/743007.png", width=80)
    st.title("🚗 Vehicle Dashboard")
    st.markdown("### 👤 Profile")
    st.write("Investor: Your Name")
    st.write("Email: your.email@example.com")
    st.markdown("---")
    page = st.radio("📊 Navigation", ["Overview", "Category Analysis", "Manufacturer Insights", "Investor Opportunities"])

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
    /* Global text color */
    body, h1, h2, h3, p, div {
        color: black !important;
    }

    /* Sidebar background and text */
    section[data-testid="stSidebar"] {
        background-color: #f0f0f0;
        color: black;
    }
    section[data-testid="stSidebar"] * {
        color: black !important;
    }

    /* Hero section */
    .hero {
        padding: 50px 20px;
        background: linear-gradient(135deg, #f5f7fa, #dfe9f3);
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 30px;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    .hero p {
        font-size: 1.2rem;
        max-width: 800px;
        margin: auto;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }

    /* Info cards */
    .info-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin: 10px;
    }
    .info-card h3 {
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
    }
    .info-card p {
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Main Content ----------------
def show_overview():
    st.markdown('<div class="hero"><h1>Welcome to the Vehicle Dashboard</h1><p>Explore vehicle registration trends, manufacturer performance, and investment opportunities.</p></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="info-card"><h3>📊 Category Analysis</h3><p>Break down registrations by 2W, 3W, and 4W with YoY and QoQ growth.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="info-card"><h3>🏭 Manufacturer Insights</h3><p>Compare market share and identify industry leaders.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="info-card"><h3>💡 Investor Opportunities</h3><p>Spot trends and make data-driven investment decisions.</p></div>', unsafe_allow_html=True)

def show_category_analysis():
    st.header("📊 Category Analysis")
    st.write("Analyze vehicle registrations by category (2W, 3W, 4W). Add charts and data here.")

def show_manufacturer_insights():
    st.header("🏭 Manufacturer Insights")
    st.write("Compare manufacturers, track market share, and explore performance metrics.")

def show_investor_opportunities():
    st.header("💡 Investor Opportunities")
    st.write("Identify growth trends and strategic investment opportunities based on vehicle data.")

# ---------------- Page Routing ----------------
if page == "Overview":
    show_overview()
elif page == "Category Analysis":
    show_category_analysis()
elif page == "Manufacturer Insights":
    show_manufacturer_insights()
elif page == "Investor Opportunities":
    show_investor_opportunities()
