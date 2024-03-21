member = int(input())
seat = list(map(int, input().split()))
cnt = 0
for i in range (member):
    if seat[i] in seat[:i]: cnt += 1
print(cnt)