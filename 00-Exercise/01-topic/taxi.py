s = int(input("请输入公里数"))
s1 = round (13 + ((s - 3) * 2.3))
s2 = round (13 + ((s - 3) * 3.45))
if 1 <= s <= 3:
    print("收费13元")
elif 4 <= s <= 15:
    print("收费", s1, "元")
elif s >= 16:
    print("收费", s2 ,"元")


