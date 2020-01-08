list01 = ["a","b","c"]


# def my_enumerate(list01):
#     index = 0
#     for item in list01:
#         yield (index,item)
#         index += 1
# # for item in my_enumerate(list01):
# #     print(item[0],item[1])
# for index,item in my_enumerate(list01):
#     print(index,item)

list02 = ["A","B","C"]
# for item in zip(list01,list02):
#     print(item)

def my_zip(list01,list02):
     for i in range(len(list01)):
         yield (list01[i],list02[i])
for item in my_zip(list01,list02):
    print(item)