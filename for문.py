# # for문 : 정해진 범위만큼 반복할 때 사용
# # for 요소 in 시퀸스: 시퀸스는 리스트, 튜플, 문자열 등을 의미 / 자바의 향상된 for문과 유사
# fruits = ["사과", "바나나", "딸기", "수박", "참외", "복숭아"]
# for e in fruits:
#     print(e, end="-")
# print()
# # for 변수 in range(시작값, 종료값, 증감값) : 자바의 일반적인 for문과 유사
# n = int(input("정수 입력 : "))
# sum = 0
# for i in range(1, n+1): #1부터 n까지 순회(종료값은 미만 개념), 증감값은 생략하면 1씩 증가
#     sum += i
# print(sum)

# # 이중 for문 사용하기
# n = int(input("정수를 입력하세요 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end=" ")
#     print()

# # 구구단 출력
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i * j}")
#     print("==============")
#

# # 이중 for문과 조건문사용
# n = int(input("정수를 입력하세요. : "))
# for i in range(0, n):
#     for j in range(0, n):
#         if j % 2 == 0:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# # for문에서 continue 사용
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i, end=" ")

# # for문을 반대로 반복하기
# for i in range(10, 0 - 1, -1): # 10부터 1씩 감소하며 0까지 출력
#     print(f"index : {i}")

# for문으로 알파벳 출력하기 :
# chr - 유니코드값을 입력받아 문자 출력)
# ord - 문자의 유니코드값을 반환
for i in range(ord("A"), ord("Z")+1):
    print(chr(i), end=" ")
print()
for i in range(65, 91): #A=65, Z=90
    print(chr(i), end=" ")





