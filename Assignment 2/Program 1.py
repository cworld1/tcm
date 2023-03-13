nums = [0, 0, 0]  # 采用列表法，使代码更精简
while True:
    for i in range(3):  # 逐个检查输入内容是否有效
        while True:
            nums[i] = input('Please input the number %s: ' % (i+1))
            try:
                nums[i] = int(nums[i])  # 如果能转成 int 类型就优先转化
            except ValueError:
                try:
                    nums[i] = float(nums[i])  # 再尝试转化位 float 类型，不能就报错重新输入
                except ValueError:
                    print('The number you input is valid. Please try again.')
                    continue
            break
    try:
        nums[2] += nums[0] / nums[1]
    except ZeroDivisionError:
        print("Some numbers can't be calculated. Please check your numbers.")
        continue  # 如果遇到 ZeroDivisionError 就要求重新输入数字
    for i in range(3):
        print('The number %s: %s' % (i+1, nums[i]))
    break  # 如果可行就打印输出并结束运行
