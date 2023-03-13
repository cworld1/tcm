import turtle

turtle.speed(10)
turtle.pensize(3)

cycle = 15
angle = 360/15
foot = 50

turtle.left(90)
for i in range(cycle):
    turtle.forward(foot)
    turtle.right(angle)
    turtle.forward(foot)
    turtle.right(180-angle)
    turtle.forward(foot)
    turtle.penup()
    turtle.right(angle)
    turtle.forward(foot)
    turtle.right(180)
    turtle.pendown()
