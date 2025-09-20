# AI Crime Assistant (MVP)

A minimal **Streamlit app** that uses **Google Gemini API** to provide general guidance for crime-related queries.

⚠️ Disclaimer: This is for **educational/demo purposes only**. It does not provide legal advice.

---

## 🚀 Setup

1. Clone or unzip the project:
   ```bash
   cd crime-assistant-gemini
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/Mac
   env\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```
