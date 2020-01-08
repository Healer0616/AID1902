for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a!=b and b!=c and c!=a:
                print(a,b,c,sep="")