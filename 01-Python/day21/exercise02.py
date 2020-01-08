"""
    为ｆｕｎ０１／ｆｕｎ０２添加计算执行时间的功能
    当前时间ｔｉｍｅ.ｔｉｍｅ（）
    执行时间：运行后时间-运行前时间
"""

import time
def print_execute_time(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        #执行原功能
        result = func(*args,**kwargs)
        execute_time = time.time() - start_time
        print(execute_time)
        return result
    return warpper

@print_execute_time
def fun01():
    time.sleep(1)
    print("fun01")

@print_execute_time
def fun02():
    time.sleep(2)
    print("fun02")

fun01()
fun02()