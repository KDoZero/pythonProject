time = list(map(int, input("시와 분을 입력하세요 : ").split(":")))
h = time[0]
m = time[1]
hm = (h * 60) + m
if hm < 45:
    whm = 1395 + hm
else:
    whm = hm - 45
wh = whm // 60
wm = whm % 60
print(f"알람 설정 시간은 {wh}시 {wm}분 입니다.")
