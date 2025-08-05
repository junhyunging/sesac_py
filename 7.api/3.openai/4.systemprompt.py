from dotenv import load_dotenv
import openai

load_dotenv()

client = openai.OpenAi()

history = []

def ask_chatgpt(user_input):
    # 가상의 인물을 만들어서 - 페르소나
    gpt_systemprompot = {'role':'system','content':'당신은 바보입니다. 질문을 이상하게 답변합니다.'}
    gpt_question = {'role':'user','content':user_input}
    if(len(history)==0):
        history.append(gpt_systemprompot)
    history.append(gpt_question)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = history,
        temperature = 0.0 #높아질수록 창의성이 높아짐 (다른 단어 후보군이 많아짐??) 소설이나 이런건 1.0~1.2 
    )
    

    gpt_response = {'role':'assistant','content':response.choices[0].message.content}
    history.append(gpt_response)
    
    return gpt_response.content



user_input = input("[you]:")
print('[챗봇응답]:', ask_chatgpt(user_input))