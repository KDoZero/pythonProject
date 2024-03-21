# num = list(map(int, input().split()))
# even, odd = [], []
# for e in num:
#     if e % 2 == 0: even.append(e)
#     else: odd.append(e)
# print(f"홀수 : {odd} \n짝수 : {even}")
num = list(map(int, input("").split()))
even = list(filter(lambda x:x % 2 == 0, num))
odd = list(filter(lambda x:x % 2 == 1, num))
print(f"홀수 : {odd} \n짝수 : {even}")