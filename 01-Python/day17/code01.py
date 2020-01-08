import time
def get_week(year,month,day):
    time_tuple = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")
    # return time_tuple[6] + 1
    week = {
        6:"星期天",
        0:"星期一",
        1:"星期二",
        2:"星期三",
        3:"星期四",
        4:"星期五",
        5:"星期六",

    }
    return week[time_tuple[6]]
print(get_week(2020,3,20))
