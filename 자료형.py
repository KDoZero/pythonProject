# 파이썬은 변수선언 시 데이터타입을 지정하지 않으며, 변수에 값이 대입될 때 형이 결정됨
# number = 200
# number2 = 3.14
# strs = ""
# bools = True
# strs = 200
# print(type(number)) # type() : 변수의 데이터형을 확인
# print(type(strs))
# print(type(bools))
# print(type(number2))

# 형변환 : 선언된 변수에 값이 할당되는 순간 형이 결정, 이 후 다른 데이터형으로 변경할 때 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(0.1 * float("512.34"))

var = "" # 공백은 거짓
number = 0 # 0은 거짓
number2 = None # 거짓
print(bool(var))
print(bool(number))
print(bool(number2))  # boolean 값의 거짓 : "", 0, None, False