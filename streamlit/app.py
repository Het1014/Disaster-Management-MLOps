import streamlit as st
import requests

API_URL = "http://api-service:8000/predict"

st.set_page_config(page_title="Disaster Message Classifier", layout="centered")

st.title("🚨 Disaster Message Classification")

message = st.text_area(
    "Enter a disaster-related message:",
    placeholder="Heavy floods have damaged houses and roads..."
)

if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner("Analyzing message..."):
            response = requests.post(
                API_URL,
                json={"message": message},
                timeout=15
            )

        if response.status_code == 200:
            result = response.json()
            st.success("Prediction successful")
            st.write("### 🏷️ Category:", result["prediction"])
            st.write("### 📊 Confidence:", round(result["confidence"], 4))
        else:
            st.error("Prediction failed. Please try again.")
