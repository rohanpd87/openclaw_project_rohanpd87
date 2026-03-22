import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.environ.get("WEATHER_KEY")
print(f"API Key: {api_key[:5]}...")