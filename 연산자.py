# 연산자 : 프로그램에 계산을 위해 사용(사칙, 대입, 비교, 관계, 비트 연산 등)
# 산술연산 : +, -, *, /, %, //(몫), **(제곱 연산자)
# 파이썬은 증감연산자 (i++, i--)가 없음
i = 10
j = 3
print(i + j)
print(i**j)
print(i / j)
print(f"{i / j :.2f}")
print(i // j)
text = "Python "
print(text * 3)

tax_rate = 0.10
income = int(input("당신의 수입은 얼마입니까? "))
print(f"당신이 내야 할 세금은 {income * tax_rate:.2f}입니다.")

# 관계(논리) 연산자
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y # &&, 둘 다 참이면 참, 거짓
rst2 = x > 0 or x > y # ||, 둘 중 하나만 참이면 참, 참
rst3 = not(x > 0 or x > y) # !, 참이면 거짓, 거짓이면 참으로 바꿈, 거짓
print(rst1, rst2, rst3)

# 3항 연산자 : (조건식) and 참일때 수행, or 거짓일때 수행
age = int(input("나이를 입력 : "))
adult = age > 19 and "성인" or "미성년자"
print(f"당신은 {adult}입니다.")

num = int(input("정수 입력 : "))
is_even = num % 2 == 0 and "짝수" or "홀수"
print(f"{num}은 {is_even}입니다.")

# 진법 표기
print(42 == 0b101010) # b => binary
print(42 == 0o52) # o => octed
print(42 == 0x2a) # x => hex
print(bin(42))
print(oct(42))
print(hex(42))

# 비트 연산자
a = 10 # 00001010
b = 12
print(a & b) # 둘 다 1이면 1
print(a | b) # 둘 중 하나만 1이면 1, 14
print(a ^ b) # 값이 다른 경우 1, 6
print(~a) # 비트 반전, 음수 표기는 2의 보수로 표기하기 때문에 1이 모자람
print(a << 1) # 주어진 값만큼 왼쪽으로 비트이동 , 20
print(a >> 1) # 5
