import os

path = os.path.dirname(__file__)  # 确认路径，避免相对路径报错

# 采用调试法检测是否能打开相应文件，同时也运行了所需代码
while True:
    firstName = str(input('The first file name: '))
    secondName = str(input('The second file name: '))
    # firstName = 'first.txt'
    # secondName = 'second.txt'
    try:
        firstFile = open(os.path.join(path, firstName), 'r')
        secondFile = open(os.path.join(path, secondName), 'r')
    except IOError:
        print('File is not accessible. Please try again.')
        continue
    break

# 先进行内容存储
first = firstFile.read()
second = secondFile.read()

# 使用写入模式写进文件并关闭
firstFile = open(os.path.join(path, firstName), 'w')
secondFile = open(os.path.join(path, secondName), 'w')
firstFile.write(second)
secondFile.write(first)
firstFile.close()
secondFile.close()
