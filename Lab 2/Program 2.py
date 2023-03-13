import os
import csv


def dictProcess(fileRead):
    '''读取内容并转化为字典'''
    dict = {}
    for line in fileRead:
        if line[0].isdigit():
            for i in range(2, 7):
                line[i] = float(line[i])
            dict[line[1]] = (tuple(line))
    return dict


def searchData(dict):
    '''导入字典内容并根据需求索引，返回指定结果'''
    while True:
        data = dict.get(input('Please input the name to search: '), 0)
        if not data:
            print("Sorry, we can't find data for that name.")
            if input('Do you want to quit?(Y) ') == 'Y':
                print('Thanks for using.')
                break
        else:
            print('''\
    Class: {0[0]:3}         | Name: {0[1]:11} |
    Homework 1:  {0[2]:>5.1f} | Hmoework 2:    {0[3]:>5.1f} | Final Exam: {0[4]:>5.1f}
    Total Score: {0[5]:>5.1f} | Average Score: {0[6]:>5.1f} |'''.format(data))


# 打开文件
path = os.path.dirname(__file__)  # 确认路径，避免相对路径报错
file = open(os.path.join(path, 'score-database-new.csv'), 'r')
fileRead = csv.reader(file)

# 建立字典并提供索引
searchData(dictProcess(fileRead))

# 关闭文件
file.close()
