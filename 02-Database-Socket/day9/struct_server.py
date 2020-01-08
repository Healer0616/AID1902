

from socket import *
import struct
import pymysql

#创建数据库游标对象
db = pymysql.connect('localhost','root','123456','eshop')
cursor = db.cursor()

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

#确定数据格式(1,b'zhangsan',8,90.5)
st = struct.Struct('i32sif')

while True:
    data,addr = s.recvfrom(1024)
    #解析数据
    data = st.unpack(data)

    stu_id = data[0]
    stu_name = data[1].decode()
    stu_age = data[2]
    stu_score = data[3]
    print(stu_id,stu_name,stu_age,stu_score)

    #插入数据库
    sql = "insert into student values(%d,'%s',%d,%f)"%(stu_id,stu_name,stu_age,stu_score)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

s.close()
db.close()