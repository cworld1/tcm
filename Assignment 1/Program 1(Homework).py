import sys

tags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 记录当前枚举的数字是否可用(1为可用，0为不可用)
# As to:0  1  2  3  4  5  6  7  8  9
letters = "SENDMORY"
num = [99, 99, 99, 99, 99, 99, 99, 99]  # 储存字母对应的替换数字

# Original: SEND + MORE = MONEY
# Position: 0123   4561   45217


def checkResult():
    # 检查填充完毕的数字是否可用

    # 当前枚举情况下的三个数
    send = num[0]*1000 + num[1]*100 + num[2]*10 + num[3]
    more = num[4]*1000 + num[5]*100 + num[6]*10 + num[1]
    money = num[4]*10000 + num[5]*1000 + num[2]*100 + num[1]*10 + num[7]

    # 判断，如果等式成立就打印结果并退出程序
    if send + more == money:
        for i in range(len(letters)):
            print('%s:%s;' % (letters[i], num[i]), end='  ')
        print('\n-----------------')
        print('%s + %s = %s' % ('SEND', 'MORE', 'MONEY'))
        print('%s + %s = %s' % (send, more, money))
        sys.exit()


def SetNumber(letterPos):
    # 对该位字母进行数字填充

    if letterPos > 7:  # 检查结束，退出程序
        return

    for testNumber in range(10):  # 给该字母测试数字(0~9)可用性

        # 不能等于 0 的号位：s(0号位)、m(4号位)
        if testNumber == 0:
            if letterPos == 0 or letterPos == 4:
                continue

        if tags[testNumber] == 1:
            num[letterPos] = testNumber
            tags[testNumber] = 0  # 如果测试的这个数字还未使用过，就先将填充给该字母，再标记为使用过状态

            if letterPos == 7:  # 如果填充完毕，则立即检查是否可用
                checkResult()

            SetNumber(letterPos+1)  # 如果没有检查出来什么的话，就继续寻找下一个字母对应数字
            tags[testNumber] = 1  # 回溯，该数字填充错误，重新标记该数字可用


SetNumber(0)  # 从0号位开始检查该字母应该填充的数字
