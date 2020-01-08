L = []
while True:
    n = int(input("请输入一个整数（-1结束): "))
    if n == -1:
        break
    L += [n]
print(L)
print("您输入的有效个数是:", len(L))
print("您输入的最大数是:", max(L))
print("您输入的最小数是:", min(L))
print("您输入的平均数是:", sum(L) / len(L))