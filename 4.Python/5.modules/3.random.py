import random as r
#무작위 숫자 만들기

print("랜덤숫자" , r.randint(1,100)) # 1부터 100까지의 양수를 다 포함하는 랜덤 숫자 생성

#주사위 던지기
def roll_dice():
    # number = r.randint(1,6)
    # return number
    return r.randint(1,6)

print(f"주사위 던진 결과:{roll_dice()}")

# 이 주사위를 100번 던져보고, 1000도 해보고, 10000번도 던져서... 각 숫자가 나올 확률을 출력해보시오
# for문으로 반복해서 결과를 취합해서 위 내용을 출력하시오
dice_count = [0, 0, 0, 0, 0, 0]
for num in range(100):
    result = roll_dice()
    dice_count[result - 1] += 1
    
print(f"1이 나온 횟수 : {dice_count[0]} 확률: {dice_count[0]/sum(dice_count)}")
print(f"2이 나온 횟수 : {dice_count[1]} 확률: {dice_count[1]/sum(dice_count)}")
print(f"3이 나온 횟수 : {dice_count[2]} 확률: {dice_count[2]/sum(dice_count)}")
print(f"4이 나온 횟수 : {dice_count[3]} 확률: {dice_count[3]/sum(dice_count)}")
print(f"5이 나온 횟수 : {dice_count[4]} 확률: {dice_count[4]/sum(dice_count)}")
print(f"6이 나온 횟수 : {dice_count[5]} 확률: {dice_count[5]/sum(dice_count)}")

# 딕셔너리 라는 자료구조이고, key:value 라는 형태로 정의해서
count2 = {i:0 for i in range(1,7)}
print(count2)




