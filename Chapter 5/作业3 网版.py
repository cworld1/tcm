import turtle  # 先导入模块
t = turtle.Pen()  # 一共定义了两个画笔，因为这样好画一些，这个画笔是画红色蓝色方框的。
b = turtle.Pen()  # 这个画笔画五角星的。
t.speed(0)  # 这个是用来显示的时候加速的。


def ct(c):  # 先画一个长条，然后在把它定义为一个函数然后好调用它
    t.color(c)  # 添加颜色
    t.begin_fill()
    for i in range(2):
        t.forward(247)  # 长条的长宽比例为 24.7 ：10
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()


for i in range(14):  # 这里画13条
    if i % 2 == 1:  # 利用数的奇数偶数的性质来给长条添加颜色
        c = 'white'
    else:
        c = 'red'
    ct(c)
    t.right(90)
    t.forward(10)
    t.left(90)
t.up()  # 因为要让画笔回到原点，所以先抬笔，然后回到原点，再放下笔
t.home()
t.down()
for j in range(4):  # 这个方框的长宽比例为 12 ：7
    t.color('blue')  # 小正方形是蓝色的。
    t.begin_fill()
    t.forward(120)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.end_fill()


def wjx():  # 先定义一个五角星，一会儿直接用来调用就可以了。
    b.color('white')
    b.begin_fill()
    for g in range(5):
        b.forward(6)
        b.left(144)
    b.end_fill()


def wjx6():  # 这是画6个一行的五角星，直接调用了之前定义的函数
    for l in range(6):
        b.up()
        b.forward(3)
        b.down()
        wjx()
        b.up()
        b.forward(18)
        b.down()


def wjx5():  # 这是画5个一行的五角星，直接调用了之前定义的函数
    for l in range(5):
        b.up()
        b.forward(10)
        b.down()
        wjx()
        b.up()
        b.forward(13)
        b.down()


b.right(90)  # 画笔运行这里时，要控制画笔的方向，这样才能更方便的控制画笔的下一步操作。
b.forward(7)
b.left(90)
for u in range(9):  # 现在用一个  for 循环来实现9行的星星
    if u % 2 == 0:  # 利用u的特性，给他个条件判断，当u整除2等于0了，就直接画6个星星，如果不等于就画5个。
        wjx6()
    else:
        wjx5()
    b.up()  # 当5个星星画完后 ，得控制画笔，让画笔回到原点，然后把画笔向右转动90度，向下平移 2倍u的7倍，然后在落笔。
    b.home()
    b.right(90)
    b.forward((u+2)*7)
    b.left(90)
    b.down()
turtle.done()  # 这个保存画面的
