#%%
from mistralai import Mistral, UserMessage
import os
from dotenv import load_dotenv
load_dotenv()
secret_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=secret_key)
model = "mistral-large-latest"

# 채팅 메시지 준비
messages = [
    {"role": "user",
     "content": "파이썬은 정말 재미있는 언어야. 를 영어로 번역해줘."},
]

# API 호출
chat_response = client.chat.complete(
    model=model,
    messages=messages
)
print(chat_response.choices[0].message.content)

# 사용자가 그만둔다는 어떤 문자를 입력하기 전까지 반복해서 사용자와 대화를 나누는 코드를 작성해보세요.

    # %%
