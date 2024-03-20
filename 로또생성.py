import random
new_list = []
for i in range(6):
    while True:
        rand = random.randint(1, 45)
        if rand not in new_list:
            new_list.append(rand)
            break
print(new_list)