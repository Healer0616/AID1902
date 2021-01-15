# -*- coding: utf-8 -*- 
# @Time    : 2021/1/3 4:53 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : ExcelImportMysql.py
# @Software: PyCharm

import xlwt, xlrd
import pymysql

data = xlrd.open_workbook("/Users/healer/Desktop/Code/aid1902/00-Exercise/Excel/saveExcel/stu.xlsx")
sheet = data.sheet_by_index(0)  # 获取到工作表
userList = []  # 构建用户列表


# 用户类
class User:
    pass


for i in range(sheet.nrows):
    obj = User()  # 构建用户对象
    obj.id = sheet.cell_value(i, 0)  # id
    obj.name = sheet.cell_value(i, 1)  # name
    obj.sfz = sheet.cell_value(i, 2)  # sfz
    userList.append(obj)

print(userList)
# 导入数据库
# 1.连接数据库
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db="test1",
    charset='utf8'
)
cursor = db.cursor()
# 插入数据操作
sql = "insert into stu(id,name,sfz) values (%s,%s,%s)"
val = []  # 空列表来存储元组
for item in userList:
    val.append((item.id, item.name, item.sfz))
print(val)
cursor.executemany(sql, val)
db.commit()  # 提交
cursor.close()  # 关闭连接
db.close()

# # 创建工作簿
# wb = xlwt.Workbook()
# # 创建工作表
# ws = wb.add_sheet("工作表1")
# # 填充数据
# # ws.write_merge(0, 1, 0, 5, "stu")
# # 写入货币数据
# data = (
#     (0, "冯志龙", 330521199709080983), (1, "张三", 330521199409080967), (2, "李四", 330521199309080587),
#     (3, "王五", 330521199209080985), (4, "朱六", 330523288798098765))
# for i, item in enumerate(data):
#     for j, val in enumerate(item):
#         ws.write(i, j, val)
# # 保存
# wb.save("/Users/healer/Desktop/stu.xlsx")
# print("保存成功")
