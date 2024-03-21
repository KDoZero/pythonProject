num = list(map(str, input().split()))
list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
print(((list.index(num[0]) * 10) + list.index(num[1])) * (10 ** list.index(num[2])))
