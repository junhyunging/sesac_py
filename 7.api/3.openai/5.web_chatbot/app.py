from flask import Flask, request, send_from_directory, jsonify

import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = openai.OpenAI()

@app.route('/')
def index():
    return send_from_directory('static','index.html')

@app.route('/api/chat',methods=['POST'])
def chat():
    data = request.get_json()
    print(data)
    userInput = data['userInput']
    chatbot_response = ask_chatgpt(userInput)
    return jsonify({"response":f"응답:{chatbot_response}"})

history = [] #이전대화 내용을 저장할 공간


def ask_chatgpt(user_input):
    # history에 저장한다.
    history.append({'role':'user','content':user_input}) 
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = history,
        temperature=1.0
    )
    
    chatgpt_response = response.choices[0].message.content
    
    history.append({'role':'user','content':chatgpt_response})
    if len(history) > 10:
        history.pop(0) # 가장 오래된거 하나 삭제
        print(history)
        print(len(history))
    
    return chatgpt_response

if __name__ == ("__main__"):
    app.run(debug=True) 