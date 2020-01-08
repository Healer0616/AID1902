def myrange(start,stop=None,step=1):
    if stop is None:
        stop = start
        start = 0
    L = []
    i = start
    while i < stop:
        L.append(i)
        i += step
    return L
L = myrange(3)
print(L)
L = myrange(2,5)
print(L)
L = myrange(4,13,2)
print(L)