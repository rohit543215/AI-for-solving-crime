import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY  # Your original API key import

st.set_page_config(page_title="AI Crime Assistant", page_icon="🕵️", layout="centered")

st.title("🕵️ AI Crime Assistance Bot (Enhanced)")
st.caption("Educational demo. Not legal advice.")

# Contextual crime-solving scenarios for better AI guide
crime_scenarios = """
You are an AI crime-solving assistant. Your task is to understand crime-related user queries and provide detailed, informative, and relevant responses with practical guidance. Use the example scenarios below to guide your answers:

Examples:

1. Scenario: A phone theft occurred. The victim wants to know next steps.
   Guidance: Recommend reporting to police immediately, providing location details, blocking the device, monitoring accounts.

2. Scenario: Cybercrime with phishing emails.
   Guidance: Suggest preserving email headers, analyzing sender IP, reporting to authorities, and educating about scams.

3. Scenario: Suspicious person in a neighborhood.
   Guidance: Advise avoiding confrontation, noting descriptions, informing local security/police, and using community alerts.

4. Scenario: Lost wallet with ID and credit cards.
   Guidance: Recommend canceling cards, reporting ID theft, monitoring credit reports, and filing a police report.

Respond clearly without providing legal advice.
"""

if not GEMINI_API_KEY or GEMINI_API_KEY == "your_api_key_here":
    st.error("⚠️ Please set your GEMINI_API_KEY in config.py to use the app.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

    query = st.text_area("Describe your issue (e.g., 'My phone got stolen')")

    if st.button("Get Guidance"):
        if query.strip():
            with st.spinner("Thinking..."):
                try:
                    model = genai.GenerativeModel("gemini-2.0-flash-lite")
                    prompt = f"""
                    {crime_scenarios}
                    User Query: {query}
                    """
                    response = model.generate_content(prompt)
                    st.subheader("🔹 Guidance")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a description before requesting guidance.")
