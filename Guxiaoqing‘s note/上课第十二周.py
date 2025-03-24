import xlrd
import xlutils.copy
import xlwt

data = xlrd.open_workbook('excelFile.xls')

table = data.sheets()[0]  # 通过索引顺序获取
table = data.sheet_by_index(0)  # 通过索引顺序获取
table = data.sheet_by_name(u'教师')  # 通过名称获取

# 获取整行和整列的值（数组）
print(table.row_values(1))
print(table.row_values(1))

# 获取行数和列数
nrows = table.nrows
ncols = table.ncols

# 循环行列表数据
for i in range(nrows):
    print(table.row_values(i))

# 循环列列表数据
for j in range(ncols):
    print(table.col_values(j))

# 获取单元格
cell_A1 = table.row(0)[0].value
cell_A2 = table.col(1)[0].value
print(cell_A1)
print(cell_A2)

# 简单的写入
row = 0
col = 0

# 类型 0 empty,1 string,2 number, 3 data, 4 boolean, 5 error
ctype = 1
value = 'STUID'
xf = 0  # 扩展的格式化
table.put_cell(row, col, ctype, value, xf)
print(table.cell(0, 0).value)  # 单元格的值

# 拷贝目标Excel文件
wtbook = xlutils.copy.copy(data)
# 保存文件
wtbook.save('AQ2.xls')

wb = xlwt.Workbook()
fruits_s = wb.add_sheet('水果')
vegetable_s = wb.add_sheet('蔬菜')
wb.save('data2.xls')

fruits_s.write(0, 0, '名称')
fruits_s.write(0, 1, '单价')
fruits_s.write(0, 2, '数量')
fruits_s.write(0, 3, '总价')

wb.save('data2.xls')  # 注意：所有写操作完成后必须保存

