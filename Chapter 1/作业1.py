import math

begin = 90000  # 初始金额（元）
endFive = round(begin*(1+0.0305*5), 2)  # 5年期
endOne = round(begin*(1+0.02)**5, 2)  # 1年期
differ = endFive - endOne  # 5年期多收入

print('''\
======= 统计结果 =======
五年期5年后总金额：%f 元
一年期5年后总金额：%f 元
五年期比一年期多收入：%f 元
=======================''' % (endFive, endOne, differ))
