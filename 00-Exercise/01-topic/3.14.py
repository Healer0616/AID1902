n = 1
sign = 1
s =0
while n <= 1000000:
    s += sign * 1 / (2 * n - 1)
    sign =sign * -1
    n += 1
print("和是:" , s)
print("和*4:", s * 4)