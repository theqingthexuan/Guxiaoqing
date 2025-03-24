

import difflib  # 读取两个文件的内容

with open('file1.txt', 'r') as f1:
    text1 = f1.read()

with open('file2.txt', 'r') as f2:
    text2 = f2.read()

# 使用 Differ 类生成两个文件的差异
diff = difflib.Differ()
diff_result = list(diff.compare(text1.splitlines(keepends=True), text2.splitlines(keepends=True)))

# 输出差异内容
for line in diff_result:
    print(line)


import difflib  # 读取两个文件的内容

with open('file1.txt', 'r') as f1:
    text1 = f1.read()

with open('file2.txt', 'r') as f2:
    text2 = f2.read()

d = difflib.HtmlDiff()
with open("passwd.html", 'w') as f:
    f.write(d.make_file(text1, text2))



