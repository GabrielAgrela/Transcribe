import requests
import time
from config import Config
from audio_saver import AudioSaver

class TextToSpeechService:
    def __init__(self, config: Config, saver: AudioSaver):
        self.config = config
        self.saver = saver

    def generate_ssml(self, text, voice_name, pitch="default"):
        return f"""
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='pt-PT'>
            <voice name='{voice_name}'>
                <prosody pitch='{pitch}'>
                    {text}
                </prosody>
            </voice>
        </speak>
        """

    def text_to_speech(self, text, output_file, voice_name, pitch="default", max_retries=3):
        ssml = self.generate_ssml(text, voice_name, pitch)
        retries = 0
        while retries <= max_retries:
            response = requests.post(self.config.url, headers=self.config.headers, data=ssml.encode("utf-8"))
            if response.status_code == 200:
                self.saver.save(response.content, output_file)
                break
            elif response.status_code == 429:
                print(f"Error: {response.status_code}, {response.text}. Retrying...")
                retries += 1
                time.sleep(2 ** retries)  # Exponential backoff
            else:
                print(f"Error: {response.status_code}, {response.text}")
                break
