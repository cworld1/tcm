# 绘图3
import turtle

# 前置
turtle.pensize(3)
turtle.speed(8)


def draw():
    for i in range(6):
        for x in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(9)


# start
turtle.left(45)
draw()
turtle.right(81)
draw()
turtle.done
