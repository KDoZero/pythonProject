# 함수로 입력받은 수가 짝수인지 홀수인지 결과 출력
def even_odd(num):
    if num % 2 == 0: print("짝수입니다.")
    else: print("홀수입니다.")

num = int(input("정수를 입력하세요 : "))
even_odd(num)

# 받은 수의 평균을 구해 반환하여 출력
def avg_func(input):
    return sum(input) / len(input)

input = list(map(int, input("정수를 입력하세요 : ").split()))
print(avg_func(input))

# 소수의 합 구하기
def prime_func(number):
    is_Prime = True
    for i in range(2, number):
        if n % 1 == 0: is_Prime = False
    if is_Prime : return number
    else: return 0

number = int(input("정수를 입력하세요 : "))
sum = 0
for i in range(2, number):
    sum += prime_func(i)
print(sum)

# 두번째 수 찾기
def second_num(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt > 0 : return i+1
            else: cnt += 1
    return -1

ls = list(map(int, input("리스트 입력 : ").split()))
n = int(input("찾는 숫자 : "))
print(second_num(ls, n))

# 세자리수 정수 입력받고 가장 큰 수 출력
a = b = c = 0
def num_split(input):
    global a, b, c
    a = input // 100
    b = (input % 100) // 10
    c = (input % 100) % 10

def compare_num():
    if a > b:
        if a < c: return a
        else: return c
    else:
        if b > c: return b
        else: return c

n = int(input())
num_split(n)
print(compare_num())