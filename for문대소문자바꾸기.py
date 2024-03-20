# 문자열을 입력받아 대문자는 소문자로, 소문자는 대문자로 변경하기
rst = ""
for e in input("단어 입력 : "):
    if e.islower():
        rst += e.upper()
    else:
        rst += e.lower()
print(rst)