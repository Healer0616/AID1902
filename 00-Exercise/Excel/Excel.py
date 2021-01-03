# -*- coding: utf-8 -*- 
# @Time    : 2021/1/3 3:37 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : Excel.py
# @Software: PyCharm

import xlrd

data = xlrd.open_workbook("/Users/healer/Desktop/test.xlsx")
# print(data.sheet_loaded(0))
# print(data.sheets())  # 获取全部工作表
# print(data.sheets()[0])  # 根据列表获取工作表
# print(data.sheet_by_index(1))  # 根据索引获取工作表
# print(data.sheet_by_name("工作表3"))  # 根据名字获取工作表
# print(data.sheet_names())  # 获取工作表名称
# print(data.nsheets)  # 获取工作表数量

# 操作Excel行
# sheet = data.sheet_by_index(2)  # 获取工作表
# print(sheet.nrows)  # 获取sheet表有效行数
# print(sheet.row(0))  # 获取该单元格对象组成的列表
# print(sheet.row_types(1))  # 获取单元格的数据类型
# print(sheet.row(0)[3].value)  # 获取该单元格value
# print(sheet.row_values(2))  # 得到指定行单元格的值
# print(sheet.row_len(1)) # 得到单元格的长度

# 操作Excel列
# sheet = data.sheet_by_index(2)
# print(sheet.ncols)
# print(sheet.col(1))
# print(sheet.col(0)[2].value)

# 操作Excel单元格
sheet = data.sheet_by_index(2)
print(sheet.cell(1, 2))
print(sheet.cell_value(1, 3))
