# pip install requests
# 더이상 빌트인 모듈이 아니고, 외부 라이브러리로 설치하는것..
# 외부는 어디냐??
# https://pypi.org/
# 이게 어디에 설치?
# 나의 파이썬 가상환경 내의 라이브러리 공간에 설치됨


import requests

resopnse = requests.get("https://www.naver.com")
print(resopnse)
print(resopnse.status_code)
print(resopnse.text)


