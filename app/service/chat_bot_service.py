import requests

from ..core import settings

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {settings.openai_api_key}"
}

def get_chatbot_response():
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
            }
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