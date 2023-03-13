from turtle import *
import math

# 国旗红条背景
# 国旗的宽度: A = 1.0
# 国旗的长度: B = 1.9


def drawRedLine(scale):
    color('#B22234')
    for i in range(7):
        goto(-0.95*scale, (0.5 - i*2/13)*scale)
        pd()
        begin_fill()
        for i in range(2):
            fd(1.9*scale)
            right(90)
            fd(1/13*scale)
            right(90)
        end_fill()
        pu()

# 联邦部分背景
# 联邦范围宽度: C = 0.5385 （7/13, 7条间纹的阔度）
# 联邦范围长度: D = 0.76 （1.9 × 2/5, 五份二的国旗长度）


def drawBlueCanva(scale):
    color('#3C3B6E')
    goto(-0.95*scale, 0.5*scale)
    pd()
    begin_fill()
    for i in range(2):
        fd(1.9*2/5*scale)
        right(90)
        fd(7/13*scale)
        right(90)
    end_fill()
    pu()

# 联邦部分星状前景
# 星的直径: K = 0.0616
# 星的纵向间距：E = F = 0.0538 （C/10, 联邦范围的十份之一阔度）
# 星的横向间距：G = H = 0.0633 （D/12, 联邦范围的十二份之一长度）


def drawOneStar(scale):  # 绘制一个五角星参考
    setheading(18)
    fd(0.0616*scale*scale2)
    setheading(180)
    pd()
    begin_fill()
    for i in range(5):
        fd(2*math.cos(18)*0.0616*scale*scale2)
        left(144)
    end_fill()
    pu()
    setheading(198)
    fd(0.0616*scale*scale2)


def drawStars(scale):
    color('#FFFFFF')
    # 第一次绘制
    goto((-0.95+0.0633)*scale, (0.5-0.0538)*scale)
    for i in range(1, 31):
        drawOneStar(scale)
        setheading(0)
        fd(2*0.0633*scale)
        if not i % 6:
            setx((-0.95+0.0633)*scale)
            setheading(270)
            fd(2*0.0538*scale)
    # 第二次绘制
    goto((-0.95+2*0.0633)*scale, (0.5-2*0.0538)*scale)
    for i in range(1, 21):
        drawOneStar(scale)
        setheading(0)
        fd(2*0.0633*scale)
        if not i % 5:
            setx((-0.95+2*0.0633)*scale)
            setheading(270)
            fd(2*0.0538*scale)


# 参数部分
scale = 200
scale2 = 0.6
speed(0)

# 绘制部分
pu()
drawRedLine(scale)
drawBlueCanva(scale)
drawStars(scale)
hideturtle()
done()
