def mysum(*args):
    return sum(args)
print(mysum(1,2,3,4))
print(mysum(2,4,6))
def mysum1(*args):
    s = 0
    for x in args:
        s += x
    return s
print(mysum1(1,2,3,4))
print(mysum(2,4,6))