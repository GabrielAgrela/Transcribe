import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.region = os.getenv("REGION")
        self.url = f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/v1"
        self.headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
            "User-Agent": "YOUR_APP_NAME",
        }
