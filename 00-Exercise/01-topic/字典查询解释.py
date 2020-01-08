zidian = {}
while True:
    a = input('请输入单词（直接回车结束)：')
    if not a:
        break
    j = input('请输入解释：')
    zidian[a] = j
while True:
    k = input('请输入要查询的词：')
    if a in zidian:
        print('解释：',zidian[a])
    else:
        print('单词不存在')