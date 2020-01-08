s = ''
s2 = ''
for i in range(65,65+26):
    s += chr(i)
    s2 += chr(i)
    s2 += chr(i + 32)
print(s)
print(s2)
