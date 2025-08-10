import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ---------------- Lottie Animation Loader ----------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Initialize session state for profile fields
if "profile_name" not in st.session_state:
    st.session_state.profile_name = "Your Name"
if "profile_email" not in st.session_state:
    st.session_state.profile_email = "your.email@example.com"
if "profile_role" not in st.session_state:
    st.session_state.profile_role = "Investor"
if "profile_bio" not in st.session_state:
    st.session_state.profile_bio = "Passionate about mobility and data-driven investments."

# ---------------- Sidebar ----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/743/743007.png", width=80)
    st.markdown("## Vehicle Dashboard")
    st.markdown("---")
    st.markdown("**👤 Profile:**")
    st.write(f"Name: {st.session_state.profile_name}")
    st.write(f"Email: {st.session_state.profile_email}")
    st.write(f"Role: {st.session_state.profile_role}")
    st.markdown("---")
    st.markdown("### 📊 Navigation")
    st.write("Use the sidebar to switch between pages.")
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

# ---------------- Page Content ----------------
st.title("👤 Profile")
st.markdown("### Your Profile Information")

# Lottie animation
lottie_profile = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")
if lottie_profile:
    st_lottie(lottie_profile, height=200, key="profile-animation")
else:
    st.warning("⚠️ Animation could not be loaded. Try with another Lottie URL.")

# Editable fields (update session state on change)
name = st.text_input("Name", value=st.session_state.profile_name, key="profile_name")
email = st.text_input("Email", value=st.session_state.profile_email, key="profile_email")
role = st.selectbox("Role", ["Investor", "Analyst", "Admin", "Guest"], 
                    index=["Investor", "Analyst", "Admin", "Guest"].index(st.session_state.profile_role), 
                    key="profile_role")
bio = st.text_area("Short Bio", value=st.session_state.profile_bio, key="profile_bio")

# Display summary
st.markdown("---")
st.markdown(f"**Name:** {st.session_state.profile_name}")
st.markdown(f"**Email:** {st.session_state.profile_email}")
st.markdown(f"**Role:** {st.session_state.profile_role}")
st.markdown(f"**Bio:** {st.session_state.profile_bio}")
st.success("✅ You can edit your profile info above. (This is a demo, info is not saved permanently.)")