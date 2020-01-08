import re

# 只匹配ASCII字符
# regex = re.compile(r"\w+",flags=re.A)

# 匹配时忽略大小写
# regex = re.compile(r"[A-Z]\w*",flags=re.I)

# 使 . 可以匹配换行
# regex = re.compile(r".+",flags=re.S)

#使 ^ $ 可以匹配每一行的开头结尾位置
regex = re.compile(r"to $",flags=re.M)

s = """Wellcome to 
北京
"""

l = regex.findall(s)
print(l)