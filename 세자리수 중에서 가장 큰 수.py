num = int(input("세자리수를 입력하세요 : "))
a = num // 100
b = (num % 100) // 10
c = num % 10

if a > b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c: print(b)
    else: print(c)
