n = int(input("정수를 입력하세요 : "))
for i in range(0, n):
    space = i
    star = n-i
    print(" " * space + "*" * star)