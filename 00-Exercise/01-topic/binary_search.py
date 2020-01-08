def binary_search(list1, item):
    """
    二分查找，递归
    :param list1:
    :param item:
    :return:
    """
    n = len(list1)
    if n > 0:
        mid = n // 2
        if list1[mid] == item:
            return True
        elif item < list1[mid]:
            return binary_search(list1[:mid], item)
        else:
            return binary_search(list1[mid + 1:], item)
    return False


def binary_search_2(list1, item):
    """
    二分查找，非递归
    :param list1:
    :param item:
    :return:
    """
    n = len(list1)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if list1[mid] == item:
            return True
        elif item < list1[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    li = [12, 24, 25, 36, 47, 48, 50, 55, 79, 80, 90, 99]
    print(binary_search(li, 55))
    print(binary_search(li, 200))
    print("*" * 20)
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 200))
