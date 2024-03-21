# 딕셔너리 : {}, 키와 값의 쌍으로 이루어짐. 자바의 HashMap과 동일 구조
# 키와 값은 콜론으로 구분
dict = {"정경수":90, "고유림":80, "나희도":89}
print(dict.keys())
print(dict.values())
print(dict.items())
print("고유림" in dict)
print("안유진" in dict)

if "고유림" in dict:
    print(dict["고유림"])

