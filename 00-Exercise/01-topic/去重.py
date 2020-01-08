L = [1,1,2,3,4,3,3,4,5,6,5,6,]
L2 = []
for x in L:
    if x not in L2:
        L2.append(x)
print(L2)