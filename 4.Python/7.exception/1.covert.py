# 구언어 방식 = if문으로 다 비교함

# 신(modern)언어의 방식은??
# try -catch, try-except 이런 형태로 변경해서 오류를 처리한다.

#이때 try 안에 오는 범위를 최소화 시킬수록 좋은것
#except 내에서 퉁~쳐서 하나로 잡지말고, 구체적으로 잡아서 핸들링 할수록 좋은것

try :
    result = 10 / 0 #crash가 발생함 .. 실행이 중단되고 프로그램이 종료되고, 더이상 다음줄로 실행할수가 없음
    print(result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
    
# 글자를 숫자로 바꾸기 
# 다른 모~~든 언어는 함수의 설명을, 그 함수 위에 씀
def convert_to_int(num_str):
#docstring 이라고 부름
    """_summary_

    Args:
        num_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    try :
        result = int(num_str)
    except ValueError:
        print("올바른 값이 아잉닙다. 입력값:" , num_str)
        result = None
        
    return result
        
    
def double_number(num):
    return num * 2

user_input = "10"

result = double_number(convert_to_int(user_input))
print(f"입력한 숫자: {user_input} 의 두배 값은 {result}입니당")