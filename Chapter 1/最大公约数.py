a = int(input('请输入数值1：'))
b = int(input('请输入数值2：'))

bigger = max(a, b)
smmaller = min(a, b)
remainder = -1

while remainder != 0:
    remainder = bigger % smmaller
    bigger = smmaller
    smmaller = remainder

print('最大公约数为', bigger)
