# 一天有86400秒
# 输入范围为（1-86400）
# 输出格式为小时，分钟和秒，以24小时表示

import re

seconds = input('请输入以秒为单位的时间点（1 ~ 86 400 之间且为整数）:')
while not re.findall('^[0-9]+$', seconds):
    seconds = input('输入内容无效。请重试：')

seconds = int(seconds)

if seconds > 1 and seconds < 86400:
    hour = seconds // 3600
    minute = seconds % 3600 // 60
    second = seconds % 3600 % 60
    print(seconds, '秒为', hour, '小时,', minute, '分钟和', second, '秒。')
else:
    print('输入内容无效。程序停止运行。')
