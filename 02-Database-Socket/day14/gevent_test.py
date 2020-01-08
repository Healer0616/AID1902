import gevent

def foo(a,b):
    print("Running foo")
    gevent.sleep(3)
    print("Foo over")

def bar():
    print("Running foo")
    gevent.sleep(2)
    print("Bar over")

f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)

gevent.joinall([f,b])
print("=================")