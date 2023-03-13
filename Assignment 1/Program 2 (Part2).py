print('Welcome to use this mini program. If you want to exit, just input the number 0.')
while True:
    print('--------------------------------')
    # 尝试输入内容，如果输入内容不能转化为int类型则报错
    try:
        A = int(input('Input your first number: '))
        B = int(input('Input your second number: '))
    except ValueError:
        print('Invalid number. Please try again.')
        continue
    # 要求 B 的数值为正
    if B < 0:
        print('Invalid number. Please try again.')
        continue
    # 退出程序方案
    if not A or not B:
        print('Exit successfully. Thanks for using.')
        break

    product = 0
    while B:
        if B % 2:
            product += A
        A *= 2
        B //= 2
    print('The product of two integers is: ', product)
