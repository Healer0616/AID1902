"""
    day9 复习
    1. for 循环：遍历可迭代对象(容器，range函数)的元素。
        与range函数结合：善于完成预定次数的循环。
        for 变量名 in range(5)   -->  0  1  2  3  4
        for 变量名 in range(4,-1,-1)   -->  4   3   2  1  0


    2. while 循环：善于完成条件循环。
             例如：小球从100m高度下落，计算弹起次数。

    3. 跳转语句：break 跳出循环体 continue 跳过本次循环，继续下次循环。

    4.容器：
        （1）字符串：由一系列字符组成的不可变序列容器，存储的是字符编码值。
           -- 编码：字符  --->  二进制
                    ASCII:包含了英文/数字/字符。每个字符1字节。
                    GBK：兼容ASCII，包含很多汉字。英文1字节，中文2字节。
                    Unicode:万国码，每个字符2字节，每个字符4字节。
                    utf-8：为了unicode存储以及传输。英文1字节，中文3字节。
           --字面值：
                转义符：改变字符的原始含义。
                       \'  \"  \"""   \\
                       \t   \n   ...
                字符串格式化：
                    字符串拼接：   “..“+变量+”...”
                    “...%s....”%(字符串变量)
                    “...%d....”%(整数变量)
                    “...%f....”%(小数变量)
                案例：02:00   01:59
                    “%02d:%02d”%(分钟,秒)
           -- 通用操作
               算数运算符：加法(拼接)   乘法(重复生成)    比较(依次比较字符串编码，发现不同返回结果)
               成员运算符：字符 in 字符串(判断字符串中是否包含字符)
               索引：获取单个字符
               切片：获取多个字符
"""
s = "abcd"
# print(s[0],s[4])  # 索引不能越界
# print(s[0:10],s[:10]) # 切片的索引值越界不报错
# print(s[1:4],s[1:]) # 起点默认为头，终点默认为尾
# print(s[:]) # 全部
# print(s[::-1]) # 倒序
# print(s[1::-1])  # ba
print(s[1:-2:-1])  # 空的
print(s[1:-1])








