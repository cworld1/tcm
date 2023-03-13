import os
import csv


def fileWrite(fileRead, newFileRead):
    '''传入原文件和新文件，进行内容补全并写入文件'''
    lastLine = ['', '', 0, 0, 0, 0, 0]
    count = 0
    for line in fileRead:
        if line[0].isdigit():
            total = float(line[2]) + float(line[3]) + float(line[4])
            line[5], line[6] = total, total/3
            for i in range(2, 7):
                lastLine[i] += float(line[i])
            count += 1
        elif line[0] == 'Averange Score':
            lastLine[0] = line[0]
            for i in range(2, 7):
                lastLine[i] /= count
            line = lastLine
        newFileRead.writerow(line)


# 打开文件
path = os.path.dirname(__file__)  # 确认路径，避免相对路径报错
file = open(os.path.join(path, 'score-database.csv'), 'r')
newFile = open(os.path.join(path, 'score-database-new.csv'), 'w', newline='')
fileRead = csv.reader(file)
newFileRead = csv.writer(newFile)

# 补全并写入文件
fileWrite(fileRead, newFileRead)

# 关闭文件
file.close()
newFile.close()
