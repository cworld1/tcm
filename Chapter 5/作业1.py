from turtle import *
import math

# 绘制画布函数


def drawCanvas(scale):
    width, height = 30 * scale, 20 * scale  # 红旗长宽比为3: 2
    pu()
    color('red')
    goto(-width/2, height/2)
    pd()
    begin_fill()
    for i in range(2):
        fd(width)
        right(90)
        fd(height)
        right(90)
    end_fill()

# 绘制5角星函数


def draw5AnglesStar(start_pos, end_pos, radius):
    # 计算参数
    side_len = radius * math.sin(math.pi/5) / math.sin(math.pi*2/5)
    left(math.degrees(math.atan2(
        end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    # 开始绘制
    pu()
    color('yellow')
    goto(start_pos)
    fd(radius)
    pd()
    right(math.degrees(math.pi * 9 / 10))
    begin_fill()
    for i in range(5):
        forward(side_len)
        left(360 / 5)
        forward(side_len)
        right(720 / 5)
    end_fill()


# 参数部分
scale = 15  # 倍率
speed(6)

# 绘制部分
drawCanvas(scale)
draw5AnglesStar(start_pos=(-10*scale, 5*scale), end_pos=(-10 *
                scale, 8*scale), radius=3*scale)
for pos in [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]:
    draw5AnglesStar(start_pos=(pos[0]*scale, pos[1]*scale),
                    end_pos=(-10*scale, 5*scale), radius=1*scale)
hideturtle()
done()
