# -*- coding: utf-8 -*- 
# @Time    : 2021/1/3 4:14 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : writeExcel.py
# @Software: PyCharm

import xlwt

titlestyle = xlwt.XFStyle()  # 初始化样式
titlefont = xlwt.Font()
titlefont.name = "宋体"
titlefont.bold = True  # 加粗
titlefont.height = 11 * 20  # 字号
titlefont.colour_index = 0x08  # 字体颜色
titlestyle.font = titlefont

# 单元格对齐方式
cellalign = xlwt.Alignment()
cellalign.horz = 0x02
cellalign.vert = 0x01
titlestyle.alignment = cellalign

# 创建工作簿
wb = xlwt.Workbook()
# 创建工作表
ws = wb.add_sheet("工作表1")
# 填充数据
ws.write_merge(0, 1, 0, 5, "2021货币兑换表", titlestyle)
# 写入货币数据
data = (
    ("日期", "英镑", "人民币", "港币"), ("01/01/2021", 8.27987, 9.232, 19738127), ("01/02/2021", 4.3232, 9.3832, 23084),
    ("01/03/2021", 83.39939, 248.234, 24234))
for i, item in enumerate(data):
    for j, val in enumerate(item):
        ws.write(i + 2, j, val)
# 保存
wb.save("/Users/healer/Desktop/Code/aid1902/00-Exercise/Excel/saveExcel/2021-货币.xlsx")
print("保存成功")
