import os

path = os.path.dirname(__file__)  # 确认路径，避免相对路径报错
file = open(os.path.join(path, 'example.txt'), 'r')

# 读第一行并初始化行数计数
count = 1
file.readline()

# 从第二行开始循环
for line in file:
    count += 1
    print('Line {:>2d} | {} ({} Words)'.format(
        count, line.strip(), len(line.split())))

file.close()
