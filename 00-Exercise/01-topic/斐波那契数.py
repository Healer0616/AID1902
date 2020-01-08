a = 0
b = 1
L = []
while len(L) < 40:
    a, b = b, a + b
    L.append(a)
print(L)