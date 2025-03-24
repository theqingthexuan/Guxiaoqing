import xlrd
import xlutils.copy
import xlwt

# 创建教师数据
teachers = [['序号', '工号', '姓名', '年龄', '性别', '身高', '体重（KG）'],
            [1, '202301', '张老师', 30, '男', 175, 70],
            [2, '202302', '茄老师', 24, '女', 178, 60]]

# 创建学生数据
students = [['序号', '学号', '姓名', '年龄', '性别', '身高', '体重（KG）'],
            [1, '202201', '朱圣炫', 20, '男', 175, 60],
            [2, '202202', '林超', 30, '男', 180, 50],
            [3, '202203', '谭志豪', 20, '男', 185, 40],
            [4, '202204', '潘家晋', 18, '女', 178, 30],
            [5, '202205', '温文斌', 19, '女', 165, 20]]

# 创建工作簿
workbook = xlwt.Workbook()

# 创建教师工作表
teachers_sheet = workbook.add_sheet('教师')

# 写入教师数据
for row_index, row_data in enumerate(teachers):
    for col_index, col_data in enumerate(row_data):
        teachers_sheet.write(row_index, col_index, col_data)

# 创建学生工作表
students_sheet = workbook.add_sheet('学生')

# 写入学生数据
for row_index, row_data in enumerate(students):
    for col_index, col_data in enumerate(row_data):
        students_sheet.write(row_index, col_index, col_data)

# 保存工作簿
workbook.save('档案表1.xls')
