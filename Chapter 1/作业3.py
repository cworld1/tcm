import math

people20 = 1443497378  # 2020 年末的人口数
birthRate = 0.0852  # 出生率
deathRate = 0.0707  # 死亡率

people21 = people20 * (1 - birthRate + deathRate)  # 2021年末的人口数
secBirth = round(people21 * birthRate / (365*24*60*60))  # 每秒出生的人数
secDeath = round(people21 * deathRate / (365*24*60*60))  # 每秒死亡的人数

print('在趋势不变的情况下，四舍五入后 2021 年每秒出生',
      secBirth, '人，死亡', secDeath, '人。')
