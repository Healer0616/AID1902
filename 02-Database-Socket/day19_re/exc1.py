import re

# pattern = r"-?\d+[/\.%]?\d*"
#
# a = "12,-13,9.8,4/9,5%,-8%,-8/9"
#
# d = re.findall(pattern,a)
# print(d)
#
#
#
#
# pattern = r"\d{4}-\d{1,2}-\d{1,2}"
#
# a = "2019-8-19"
#
# d = re.findall(pattern,a)
# print(d)
# s = re.sub(r"-",".",a)
# print(s)

f = open("test")
data = f.read()

# 大写字母开头单词
# regex = re.compile(r"\b[A-Z]+[a-z]*\b")

# 匹配数字
# regex = re.compile(r"\s(-?\d+\.?/?\d*%?)")

#替换日期
regex = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")

for i in regex.finditer(data):
    # print(i.group())
    print(re.sub(r"-",".",i.group()))

# l = regex.findall(data)
# print(l)