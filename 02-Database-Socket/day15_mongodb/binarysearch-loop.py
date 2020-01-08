# 扑克牌54，只取红桃13张用1 - 13，将13张牌从小到大排列然后翻面朝上。找到红桃6.怎么找？

# 二分查找

# 使用循环实现

# 原始数据 value
# [1,2,3,4,5,6,7,8,9,10,11,12,13]
# 待查找数据 key - 6
def binary(value, key):
    # 获取左侧、右侧数据对应下标值
    left = 0
    right = len(value) - 1

    # 如果存在合法范围则继续
    while left <= right:
        # 获取中间数据对应下标值
        middle = (left + right) // 2
        # 比较中间数据值与待查找数据
        if value[middle] == key:
            # 中间数据值与待查找数据相等
            # 查找成功，返回对应下标值
            return middle
        elif value[middle] > key:
            # 中间数据值大于待查找数据时
            # 继续在左侧重复查找
            # 查找范围缩小：左侧不变，右侧变为中间的前一位
            right = middle - 1
        else:
            # 中间数据值小于待查找数据时
            # 继续在右侧重复查找
            # 查找范围缩小：右侧不变，左侧变为中间的后一位
            left = middle + 1
    # 查找失败，返回-1
    return -1



if __name__ == "__main__":
    # 原始数据 value
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # 待查找数据 key
    key = 6
    # 调用二分查找
    res = binary(value, key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功", res)