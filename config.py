import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDS1eX3N87N7yCYHK5cZT17LI7KGyPW4Dc")
