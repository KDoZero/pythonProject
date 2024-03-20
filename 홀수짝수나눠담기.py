num = list(map(int, input().split()))
list1, list2 = [], []
for e in num:
    if e % 2 == 0: list2.append(e)
    else: list1.append(e)
print(f"홀수 : {list1} \n짝수 : {list2}")