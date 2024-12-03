import streamlit as st
import pandas as pd
from mistralai import Mistral, UserMessage


st.title("첫 스트림릿 예제")
st.write('안녕하세요, 처음 만드는 스트림릿 예제입니다.')

st.write(
    pd.DataFrame(
        {
            'A': [1, 2, 3, 4],
            'B': [10, 20, 30, 40]
        }
    )
)

# st.line_chart(
#     pd.DataFrame(
#         {
#             '컬럼1': [1, 2, 3, 4],
#             '컬럼2': [10, 20, 30, 40]
#         }
#     )
# )
x = st.slider("x")
st.write(x, 'squared is', x * x)

st.sidebar.write("사이드바에 텍스트를 작성합니다.")
st.slider("슬라이더를 테스트합니다.", 0, 100, 50)
st.button("버튼을 눌러보세요.")
st.checkbox("체크박스를 테스트합니다.")
st.radio("라디오 버튼을 테스트합니다.", ["옵션1", "옵션2", "옵션3"])
import os

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
st.write(chat_response.choices[0].message.content)