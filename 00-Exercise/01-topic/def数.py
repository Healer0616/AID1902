def input_number():
    L = []
    while True:
        s = int(input('请输入整数，输入负数结束：'))
        if s < 0:
            
            return L
        L.append(s)
def _shu_():
    L = input_number()
    print(L)
    print('用户输入的最大数是：', max(L))
    print('用户输入的最小数是：', min(L))
    print('用户输入的和是：', sum(L))
_shu_()