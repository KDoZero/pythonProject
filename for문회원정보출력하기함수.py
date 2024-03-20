# 회원 정보 출력 하기 (1단계는 현재 상태대로 -> 함수 형태로)
def input_age():
    while True:
        age = input("나이를 입력하세요. : ")
        if age.isdigit(): # 문자열이 숫자로 구성되었는지 확인
            age = int(age)
            if 0 < age < 200: return age
        print("나이를 잘 못 입력했습니다.")
def input_gender():
    while True:
        gender = input("성별을 입력하세요; : ")
        if gender == "M" or gender == "m": return "남성"
        elif gender == "F" or gender == "f": return "여성"
        print("성별을 잘 못 입력했습니다.")
def input_jobs():
    while True:
        jobs = input("직업을 입력하세요. : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘 못 입력했습니다.")
# []리스트, {}딕셔너리, ()튜플
def print_info(name, age, gender, jobs):
    jobs_str = "", "학생", "회사원", "주부", "무직" # 튜플
    print("=" * 3, "회원정보", "=" * 3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"
# 함수 호출과 파일 저장하기
fd = open("member.txt", "wt", encoding="utf-8")
while True:
    name = input("이름을 입력하세요.(종료하려면 quit) : ")
    if name == "quit": break
    age = input_age()
    gener = input_gender()
    jobs = input_jobs()
    rst = print_info(name, age, gener, jobs)
    fd.write(rst + "\n")
fd.close()