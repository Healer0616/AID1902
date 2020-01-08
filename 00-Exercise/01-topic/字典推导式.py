Nos = [1001,1002,1003,1004]
names = ['Tom','Jerry','Spike','Tyke']
d = {Nos[i] : names[i] for i in range(min(len(Nos),len(names)))}
print(d)