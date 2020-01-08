tuple01 = ("悟空","八戒","唐僧","沙僧","女儿国国王")
dict01 = {"悟空":2000,"八戒":3000,"唐僧":1000,"沙僧":2800}

iterator = tuple01.__iter__()
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break

print(".............")


iterator01 = dict01.__iter__()
while True:
    try:
        key = iterator01.__next__()
        value = dict01[key]
        print(key,value)
    except StopIteration:
        break