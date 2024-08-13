import requests
import time

contents = "안녕하세요. 반갑습니다."
# contents = "내가 그린 기린 그림은 잘 그린 기린 그림이고 네가 그린 기린 그림은 못 그린 기린 그림이다."
contents = '안촉촉한 초코칩 나라에 살던 안촉촉한 초코칩이 촉촉한 초코칩 나라의 촉촉한 초코칩을 보고 촉촉한 초코칩이 되고 싶어서 촉촉한 초코칩 나라에 갔는데 촉촉한 초코칩 나라의 촉촉한 초코칩 문지기가 "넌 촉촉한 초코칩이 아니고 안촉촉한 초코칩이니까 안촉촉한 초코칩 나라에서 살아"라고해서 안촉촉한 초코칩은 촉촉한 초코칩이 되는것을 포기하고 안촉촉한 초코칩 나라로 돌아갔다.'

melo_tts_url = f"http://127.0.0.1:8000/api/v1/tts/melo?contents={contents}"
openai_tts_url = f"http://127.0.0.1:8000/api/v1/tts/openai?contents={contents}"

execution_time_list = []
for _ in range(10):
    start_time = time.time()

    response = requests.get(openai_tts_url)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Response: {response}")
    print(f"Execution time: {execution_time} seconds")
    execution_time_list.append(execution_time)

avg_time = sum(execution_time_list) / len(execution_time_list)
print(f"Avarage execution time: {avg_time} seconds")