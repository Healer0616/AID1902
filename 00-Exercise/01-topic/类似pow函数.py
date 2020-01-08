def mysum(a,b,c=0):
    if c == 0:
        return a + b
    return (a + b) % c
print(mysum(1,100))
print(mysum(2,10,7))    