import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)

# 获取match对象
obj = regex.search("abcdefghi")

# **************属性变量******8
print(obj.pos)         # 匹配目标字符串开始位置
print(obj.endpos)      # 匹配目标字符串结束位置
print(obj.re)          # 正则表达式
print(obj.string)      # 目标字符串
print(obj.lastgroup)   # 最后一组的组名
print(obj.lastindex)   # 最后一组的序号
print("==============================")
print(obj.start())     # 获取匹配内容的开始位置
print(obj.end())       # 获取匹配内容的结束位置
print(obj.span())      # 获取匹配内容的起止位置
print(obj.groupdict()) # 获取捕获组组名和对应内容的字典
print(obj.groups())    # 获取子组对应内容
print(obj.group())
print(obj.group(1))
print(obj.group("pig"))