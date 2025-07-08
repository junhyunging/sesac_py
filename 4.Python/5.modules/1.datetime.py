# https://docs.python.org/ko/3.10/library/datetime.html
# 빌트인 모듈 (built-in moducle) - 추가 설치 하지 않아도 바로 쓸 수 있음

import datetime as dt


# 모듈명.변수명
# 모듈명.함수명.변수명

#현재 시간 가져오기
now = dt.datetime.now().strftime('%Y-%m-%d')
now = dt.datetime.now().strftime('%H-%M-%S')
# yyyy-mm-dd HH:MM:SS.MMMMM

print(now)

print(dt.MINYEAR)
print(dt.MAXYEAR)

#내가 특정 날짜를 정해서 해당 시간값을 담아놓고 싶으면?
my_time = dt.datetime(2025,6,30,10,46,00) #현재시간을 담아줌
print(my_time)

