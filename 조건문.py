# # 조건문과 반복문은 제어문이라고 하고, 이는 순차적인 흐름을 제어하는 목적으로 사용
# # 파이썬의 조건문은 자바의 if문과 switch문을 결합한 형태와 유사, 파이썬은 switch문이 없음
# # 조건문의 수행은 들여쓰기 구분하고 각각의 조건은 :(클론)으로 구분
# num = int(input("정수를 입력하세요. : "))
# if num > 100:
#     print("입력값이 100보다 커요.")
# elif num < 100:
#     print("입력값이 100보다 작아요.")
# else:
#     print("입력값은 100과 같아요.")
#
# season = input("지금 계절은? ")
# if season == "spring":
#     print("따듯한 봄입니다.")
# elif season == "summer":
#     print("무더운 여름입니다.")
# elif season == "fall" or season == "autumn":
#     print("쓸쓸한 가을입니다.")
# else:
#     print("추운 겨울입니다.")

# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력받아 평균을 구해 등급 출력하기
# 평균이 90이상이면 A, 80이상 B, 70이상 C, 60이상 D, 나머지는 F
score = list(map(int, input("국어, 영어, 수학 점수를 입력하세요. : ").split()))
avg = sum(score)/len(score)
if avg >= 90: print("A학점 입니다.")
elif avg >= 80 and avg < 90: print("B학점 입니다.")
elif avg >= 70 and avg < 80: print("C학점 입니다.")
elif avg >= 60 and avg < 70: print("D학점 입니다.")
else: print("F학점 입니다.")