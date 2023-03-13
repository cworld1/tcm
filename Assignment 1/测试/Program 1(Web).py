# https://blog.csdn.net/weixin_36261225/article/details/103579564
# addition send + more = money
"""
  S E N D
+ M O R E
_________
M O N E Y
"""
import time
start = time.time()


def checknospecialword(str_1, str_2, str_3):  # check repeat word in two addition
    checking = str_2+str_3
    for i in range(len(checking)):
        if str_1 == checking[i]:
            return False
    return True


def checknorepetwords(varible):  # define method to check no repeat word
    for i in range(len(varible)):
        checking = varible[i]
        for j in range(i + 1, len(varible)):
            if checking == varible[j]:
                return False

    return True


for i in range(10000, 100000):
    result = str(i)
    if checknorepetwords(result):
        for r in range(10):
            x2 = result[0] + result[1] + str(r) + result[3]
            if checknorepetwords(x2):
                for s in range(1, 10):
                    for d in range(10):
                        x1 = str(s) + result[3] + result[2] + str(d)
                        if checknorepetwords(x1):
                            if int(x1) + int(x2) == i:
                                if checknospecialword(x1[0], x2, result):
                                    if checknospecialword(x1[3], x2, result):
                                        if checknospecialword(x2[2], x1, result):
                                            if checknospecialword(result[4], x1, x2):
                                                print("The answer is:", x1,
                                                      " + ", x2, " = ", result)
                                                print(time.time()-start)
