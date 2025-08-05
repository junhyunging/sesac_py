import os
from dotenv import load_dotenv

# from langchain.llms import Openai # 구버전용
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI() # gpt-3.5가 기본값

# instruct # 시키는 모델,문장 완성형 모델
# gpt turbo #채팅,사용자와 인터렉션, QA 모델...
# 두개 모델의 차이를...

prompt = ""

result = llm.invoke(prompt)
print(result)

