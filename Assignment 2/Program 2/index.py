import os
from posixpath import split

path = os.path.dirname(__file__)  # 确认绝对路径，避免相对路径报错

source = open(os.path.join(path, 'source.txt'), 'r')
processed = open(os.path.join(path, 'processed.txt'), 'w')

content = source.read().lower().split()
for i in range(20):
    processed.write(content[i].strip(',.'))

    # 如果一行满了 5 个就换行，否则加空格隔开
    processed.write('\n') if i % 5 == 4 else processed.write(' ')
