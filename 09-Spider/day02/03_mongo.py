import pymongo

# 3个对象
conn = pymongo.MongoClient("localhost",27017)
db = conn['maoyandb']
myset = db['filmset']
# 执行插入语句
myset.insert_one({'name':'Tiechui'})
# insert_many()
myset.insert_many([{'name':'周芷若'},{'name':'赵敏'}])