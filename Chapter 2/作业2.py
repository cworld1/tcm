import math
import turtle

# 定义
start, end = -100, 100
# 函数：f(x) = ax**2
a = 0.01  # 控制幅度系数a的值

# 绘制坐标图
turtle.penup()
turtle.goto(1.2*start, 0)
turtle.pendown()
turtle.goto(1.2*end, 0)
turtle.write('x')
turtle.penup()
turtle.goto(0, -1.2*a*start**2)
turtle.pendown()
turtle.goto(0, 1.2*a*start**2)
turtle.write('y')
turtle.penup()

# 绘制图像
turtle.goto(start, a*start**2)
turtle.pendown()
for x in range(start, end):
    turtle.goto(x, a*x**2)

turtle.done()
