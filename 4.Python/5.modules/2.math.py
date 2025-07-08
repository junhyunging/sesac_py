#https://docs.python.org/ko/3.10/library/math.html?highlight=math#module-math
import math

print(math.pi)

# 원의 넓이를 구할거임
# pi * radius ^ 2

radius = 5

area = math.pi * radius ** 2
area2 = math.pi * math.pow(radius, 2)
print(f"[{area2}]") # :.2f 소수 둘째자리까지 표시

