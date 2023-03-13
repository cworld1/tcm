import turtle
import math
num_times = 15

# 红旗长宽比为3: 2
width, height = 30 * num_times, 20 * num_times
# 初始化屏幕和海龟对象
turtle.hideturtle()
turtle.speed(6)

turtle.penup()
turtle.goto(-width/2, height/2)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.fd(width)
turtle.right(90)
turtle.fd(height)
turtle.right(90)
turtle.fd(width)
turtle.right(90)
turtle.fd(height)
turtle.right(90)
turtle.end_fill()

# 画5角星


def draw5AnglesStar(start_pos, end_pos, radius):
    side_len = radius * math.sin(math.pi/5) / math.sin(math.pi*2/5)
    turtle.left(math.degrees(math.atan2(
        end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    turtle.penup()
    turtle.goto(start_pos)
    turtle.fd(radius)
    turtle.pendown()
    turtle.right(math.degrees(math.pi * 9 / 10))
    turtle.begin_fill()
    turtle.fillcolor('yellow')
    for i in range(5):
        turtle.forward(side_len)
        turtle.left(360 / 5)
        turtle.forward(side_len)
        turtle.right(720 / 5)
    turtle.end_fill()


draw5AnglesStar(start_pos=(-10*num_times, 5*num_times), end_pos=(-10 *
                num_times, 8*num_times), radius=3*num_times)
for pos in [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]:
    draw5AnglesStar(start_pos=(pos[0]*num_times, pos[1]*num_times),
                    end_pos=(-10*num_times, 5*num_times), radius=1*num_times)

turtle.done()
