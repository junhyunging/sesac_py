x= 5
y = "hello"
z = [1,2,3]

print(type(x))
print(type(y))
print(type(z))

#print(y.upper()) # 각각의 변수 타입은 클래스로 만들어져 있고, 그 안에
#있는 함수를 통해서 세부 클래스의 함수들이 동작한다.

print(isinstance(x,int)) # x는 int로 만들어진거야?

class A :
     pass #아무것도 안해도 됨 일딴 끝
 
class B(A) : # B extends A (A를 상속 받았음)
     pass
 
class C:
     pass
 
b = B() # b= new B(), b라는 변수를 B라는 클래스로 찍어냄

print(isinstance(b,A))
print(isinstance(b,B))
print(isinstance(b,C))

a = A()
print(isinstance(a,A))
print(isinstance(a,B))
print(isinstance(a,C))

 
 