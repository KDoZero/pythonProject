n = int(input("정수를 입력하세요 : "))
for i in range(1, n * n + 1):
    print(f"{i:3}",end=" ")
    if i % n == 0: print()