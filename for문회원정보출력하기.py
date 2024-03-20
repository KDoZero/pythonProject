name = input("이름을 입력하세요 : ")
while True:
    age = int(input("나이를 입력하세요 : "))
    if 0 <= age < 200: break
    print("범위를 벗어났습니다. 다시 입력해주세요.")
while True:
    gender = input("성별을 입력하세요.(M/m or F/f) : ")
    if gender == "M" or gender == "m":
        rst_gender = "남"
        break
    elif gender == "F" or gender == "f":
        rst_gender = "여"
        break
    print("범위를 벗어났습니다. 다시 입력해주세요.")
while True:
    job = int(input("직업을 선택해주세요.1(학생), 2(회사원), 3(주부), 4(무직) : "))
    if job == 1:
        rst_job = "학생"
        break
    if job == 2:
        rst_job = "회사원"
        break
    if job == 3:
        rst_job = "주부"
        break
    if job == 4:
        rst_job = "무직"
        break
    print("범위를 벗어났습니다. 다시 입력해주세요.")
print(f"이름 : {name} \n나이 : {age} \n성별 : {rst_gender} \n직업 : {rst_job}")