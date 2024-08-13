import requests
from dotenv import load_dotenv
import os
import io

load_dotenv()
api_key=os.environ.get('OPENAI_API_KEY')

url = "https://api.openai.com/v1/audio/speech"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def convert_text_to_speech_openai(contents: str) -> io.BytesIO:
    data = {
        "model": "tts-1",
        "input": contents,
        "voice": "alloy"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # 음성 데이터를 바로 반환합니다.
        audio_data = response.content
        buffer = io.BytesIO(audio_data)
        return buffer
    else:
        raise Exception(f"Failed to convert text to speech: {response.status_code}, {response.text}")
