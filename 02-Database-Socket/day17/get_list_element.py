list1 = [1, 2, [34, 55, ["123", 9]]]

def fun(ls):
    for i in ls:
        if isinstance(i, list):
            fun(i)
        else:
            print(i)


fun(list1)
