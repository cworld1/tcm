import math
import turtle

# 定义
start = -175
end = 175
# 函数：f(x) = a sin(kx+b)  (k=2pi/T)
T = (end-start)/3.5
k = 2*math.pi/T
a = 50

# 绘制坐标图
turtle.penup()
turtle.goto(1.2*start, 0)
turtle.pendown()
turtle.goto(1.2*end, 0)
turtle.write('x')
turtle.penup()
turtle.goto(0, -1.5*a)
turtle.pendown()
turtle.goto(0, 1.5*a)
turtle.write('y')
turtle.penup()

# 绘制 cosx 图像
turtle.pencolor('red')
turtle.goto(start, 0)
turtle.pendown()
for x in range(start, end+1):
    turtle.goto(x, a*math.sin(k*(x-start+T/2)))
turtle.penup()

# 绘制 sinx 图像
turtle.pencolor('blue')
turtle.goto(start, a)
turtle.pendown()
for x in range(start, end+1):
    turtle.goto(x, a*math.sin(k*(x-start+T/4)))
turtle.penup()

# 标注点
turtle.goto(-100, -15)
turtle.write("-2\u03c0")  # 提示 -2Π
turtle.goto(100, -15)
turtle.write("2\u03c0")  # 提示 2Π

turtle.hideturtle()
turtle.done()
