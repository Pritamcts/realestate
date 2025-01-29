import requests
import streamlit as st

webhook_url = "https://agentic.prach.org/webhook-test/d7f685fa-9b29-4a1a-8d65-03812f07bec6"

# Set up the app title and description
st.set_page_config(page_title="Real Estate", page_icon="🌍", layout="centered")

st.title("Real Estate")
st.write("Please enter your email and the location below.")

# Input fields
email = st.text_input("Email", placeholder="Enter your email")
location = st.text_input("Location", placeholder="Enter your location")

# Submit button
if st.button("Submit"):
    if email and location:
        payload = {
            "email" : email,
            "location" : location
        }
        try:
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status()  
            print("Success:", response.text)
            st.success(f"Please check your mailbox for info about the property at : {location} ")
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            st.error(f"Error:{e}")

    else:
        st.warning("⚠️ Please fill out both fields.")

# Style customization
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)
