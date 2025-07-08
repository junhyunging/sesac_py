# pip install bs4
 # pip install requests
# 더이상 빌트인 모듈이 아니고, 외부 라이브러리로 설치하는것..
# 외부는 어디냐??
# https://pypi.org/
# 이게 어디에 설치?
# 나의 파이썬 가상환경 내의 라이브러리 공간에 설치됨


import requests
from bs4 import BeautifulSoup # 안에 라이브러리 안에있는 특정 객체만 가져오기

resopnse = requests.get("https://www.naver.com")
print(resopnse)
print(resopnse.status_code)
print(resopnse.text)

# 여기 위에는 그냥 문자열이고..
# 여기 아래는 문자를 파싱해서, DOM의 형태로 자료구조를 갖추고 있음..

#HTML 을 파싱해서주는 라이브러비

soup = BeautifulSoup(resopnse.text, "html.parser")
print(soup)
head = soup.find("head")
print("헤드DOM은:",head)

body = soup.find("body")
print("바디DOM:", body)

bodytext = body.text.strip() #문자열 가져와서 불필요한 공백 제거
print("바디내용은:", bodytext)






