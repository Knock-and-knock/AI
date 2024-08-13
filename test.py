import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.environ.get('OPENAI_API_KEY')

# 요청 URL
url = "https://api.openai.com/v1/chat/completions"

# 요청 헤더 설정
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 요청 데이터 설정
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "2020년에 월드컵 우승팀이 어디야?"
        },
        # {
        #     "role": "assistant",
        #     "content": "The Los Angeles Dodgers won the World Series in 2020."
        # },
        # {
        #     "role": "user",
        #     "content": "Where was it played?"
        # }
    ]
}

# POST 요청 보내기
response = requests.post(url, headers=headers, json=data)

# 응답 출력
print(response.json())

# JSON 응답 파싱
response_data = response.json()

# 응답 메시지에서 답변 내용 추출
message = response_data['choices'][0]['message']['content']

# 추출된 메시지 출력
print(message)