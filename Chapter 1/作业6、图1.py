import turtle

# 调整效果
turtle.pensize(3)
turtle.speed(4)

# 准备工作


def lft():
    turtle.forward(20)
    turtle.left(90)


def rht():
    turtle.forward(20)
    turtle.right(90)


def lftTurn():
    lft()
    lft()
    rht()
    turtle.forward(20)
    rht()
    rht()
    lft()
    lft()
    rht()
    rht()
    turtle.forward(20)
    rht()
    lft()
    lft()
    turtle.forward(20)


def rhtTurn():
    rht()
    rht()
    lft()
    turtle.forward(20)
    lft()
    lft()
    rht()
    rht()
    lft()
    lft()
    turtle.forward(20)
    lft()
    rht()
    rht()
    turtle.forward(20)


turtle.penup()
turtle.goto(70, 70)
turtle.pendown()
turtle.left(180)

# 画图
lftTurn()
lft()
rhtTurn()
turtle.forward(20)
rhtTurn()
turtle.left(90)
turtle.forward(20)
lftTurn()

turtle.done()
