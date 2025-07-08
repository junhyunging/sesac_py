# *별찍기
#print("*")
#print("**")


def drow_triangle(lines):
    for i in range(1,lines+1):
      print(i * "*")

drow_triangle(5)

#오른쪽으로 붙여서 별찍기
def draw_ltriangle(lines):
    for i in range(1, lines + 1):
        print(" " * (lines - i) + "*" * i)
draw_ltriangle(5)


#역삼각형 unverse
def draw_iltriangle(lines):
    for i in range (lines, 0, -1):
        print(" " * (lines - i) + "*" * i)

draw_iltriangle(5)



