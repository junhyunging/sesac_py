import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate

text = "Python 개발"

client_id =  os.getenv("NAVER_CLIENT_ID") # 여기에 발급받은 ID/Secret 을 입력
client_secret = os.getenv("NAVER_CLIENT_SECREY")

encText = requests.utils.quote(text)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText

headers = {
"X-Naver-Client-Id",client_id,
"X-Naver-Client-Secret",client_secret
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    response_body = response.text
    # print(response_body)
    
    data  = json.loads(response_body)
    
    selected_columns = [["title","link","description"]]
    for item in data["items"]:
        # print(item['title'],item['link'])
        selected_columns.append([item['title'],item["link"],item["description"]])
    