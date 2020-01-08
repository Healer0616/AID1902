

def verify_permission(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        #if 条件执行
        return func(*args,**kwargs)
    return wrapper

@verify_permission
def enter_backround():
    print("进入后台系统...")

@verify_permission
def delete_order(order_id):
    print("删除订单",order_id)

enter_backround()
delete_order(101)
