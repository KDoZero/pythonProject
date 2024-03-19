type = input("주간근무[1], 야간근무[2]를 입력 하세요 : ")
time = int(input("근무 시간을 입력해 주세요 : "))
pay = int(9620)
if type == "주간근무" or type == "1":
    print(f"입력한 시간 동안 근무한 주간 급여는 {pay * time}원 입니다.")
elif type == "야간근무" or type == "2":
    print(f"입력한 시간 동안 근무한 야간 급여는 {pay * time * 1.5}원 입니다.")
