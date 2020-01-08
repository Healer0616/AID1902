names = ['a','b','c','d']
s = set(names)
L = []
for x in s:
    tishi = x + '已到?(y):'
    i = input(tishi)
    if i != 'y':
        L.append(x)
print('未到场的是：')
for x in L:
    print(x,end=' ')
print()