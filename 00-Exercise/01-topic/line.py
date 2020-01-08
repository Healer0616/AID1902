a = input("请输入第1个字符串:")
b = input("请输入第2个字符串:")
c = input("请输入第3个字符串:")
m = len(a)
if len(b) > m:
    m = len(b)
if len(c) > m:
    m = len(c)
print(m)
line1 = ("+" + "-" * (m + 2) + "+")
print(line1)
left = (m - len(a)) // 2
right = m - len(a) - left
line = '| ' + ' ' * left + a + ' ' * right + ' |'
print(line)
left = (m - len(b)) // 2
right = m - len(b) - left
line = '| ' + ' ' * left + b + ' ' * right + ' |'
print(line)
left = (m - len(c)) // 2
right = m - len(c) - left
line = '| ' + ' ' * left + c + ' ' * right + ' |'
print(line)
print(line1)