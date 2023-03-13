import turtle

# 定义 3 个输入值相同的变量：
# begin 不会再改变并用于确定初始和结束的位置
# test 用于试运行并知晓行走步数
# number 用于实际运行
begin = test = number = int(input('Give me the number you want: '))
counter = 0

if number <= 1:
    print('Sorry. We cannot calculate the number you give.')
    exit()

while test != 1:
    if not test % 2:
        test /= 2
    elif test % 2:
        test = test*3 + 1
    counter += 1  # 记录步数

stepX = 500//counter  # 优化显示效果，使无论输入什么值，图像在左右边界上都处在合适的位置
turtle.speed(9)  # 提升运行速度

turtle.penup()
turtle.setposition(-(counter//2)*stepX, number - begin//2)
turtle.pendown()
turtle.write(number)
for i in range(-(counter//2)*stepX + stepX, -(counter//2)*stepX + counter*stepX+1, stepX):
    if number % 2 == 0:
        number /= 2
    elif number % 2:
        number = number*3 + 1
    turtle.goto(i, number - begin//2)
    turtle.write(number)
    print(number)  # 方便后台查看运行情况
turtle.done()
