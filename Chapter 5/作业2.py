from turtle import *
import random


def drawArrow(x, y, scale):
    # 计算数值
    begin = {x: random.randint(-30*scale, 30*scale),
             y: random.randint(-30*scale, 30*scale)}
    direction = 0
    if begin[x] >= 0 and begin[y] >= 0:
        direction = random.randint(180, 270)
    elif begin[x] < 0 and begin[y] >= 0:
        direction = random.randint(270, 360)
    elif begin[x] < 0 and begin[y] < 0:
        direction = random.randint(0, 90)
    elif begin[x] >= 0 and begin[y] < 0:
        direction = random.randint(90, 180)
    # 绘制坐标
    setheading(0)
    color('Black')
    goto(x-50*scale, y)
    pd()
    goto(x+50*scale, y)
    write('x')
    pu()
    goto(x, y-50*scale)
    pd()
    goto(x, y+50*scale)
    write('y')
    pu()
    # 绘制箭头
    color(colorList[random.randint(0, 6)])
    goto(x + begin[x], y + begin[y])
    pd()
    setheading(direction)
    fd(random.randint(40*scale, 60*scale))
    pu()
    rt(150)
    fd(10*scale)
    rt(180)
    pd()
    fd(10*scale)
    lt(120)
    fd(10*scale)
    pu()


# 参数部分
scale = 1.5
colorList = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']
speed(6)
hideturtle()
count = -360*scale
pu()
for i in range(0, 20):
    if not (i) % 4:
        count += 120*scale
    drawArrow(count, (120*(i % 4)-180)*scale, scale)
done()
