a0 = dict(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5)))
a1 = range(10)
a2 = [i for i in a1 if i in a0]
a3 = [a0[s] for s in a0]
a4 = [i for i in a1 if i in a3]
a5 = {i: i * i for i in a1}
a6 = [[i, i * i] for i in a1]
print(a0)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


f(2)
f(3, [3, 2, 1])
f(3)
