import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def check_url(url):
    url_vector = vectorizer.transform([url])
    prediction = model.predict_proba(url_vector)[0]
    phishing_prob = prediction[0]
    safe_prob = prediction[1]
    return safe_prob * 100, phishing_prob * 100

# UI
st.set_page_config(page_title="Phishing Website Detector", page_icon="🔍")
st.title("🔐 Phishing Website Detector")
st.write("Enter a URL to check how safe it is:")

url_input = st.text_input("🔗 URL:")

if st.button("Check Safety"):
    if url_input:
        safe, phishing = check_url(url_input)
        st.write(f"✅ **Safety Score:** {safe:.2f}%")
        st.write(f"⚠️ **Phishing Probability:** {phishing:.2f}%")
        if safe > 50:
            st.success("This website is likely SAFE.")
        else:
            st.error("⚠️ This website may be a PHISHING site!")
    else:
        st.warning("Please enter a URL.")
