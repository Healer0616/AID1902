
def print_func_name(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper

#目的：拦截对被装饰方法的调用
@print_func_name  #say_hello = print_func_name(say_hello)
def say_hello(name):
    print(name,"hello")

@print_func_name  #say_goodbey = print_func_name(say_goodbey)
def say_goodbey(name):
    print(name,"goodbey")

say_hello("张三")
say_goodbey("李四")