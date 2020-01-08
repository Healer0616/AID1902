import pymysql

# 创建2个对象
db = pymysql.connect(
    'localhost', 'root', '123456', 'maoyandb',
    charset='utf8'
)
cursor = db.cursor()
# 执行数据库插入
ins = 'insert into filmset values(%s,%s,%s)'
data_list = [
    ['大话西游','周星驰','1994'],
    ['喜剧之王','周星驰','2000']
]
cursor.executemany(ins, data_list)

db.commit()
cursor.close()
db.cursor()

