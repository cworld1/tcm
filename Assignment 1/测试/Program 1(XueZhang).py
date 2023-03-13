'''
通过函数实现深搜与剪枝(不直接枚举出八个字母的值，当枚举一部分发现已经是不可能时，直接排除这种情况)，
在较短时间内实现破译每个字母对应的数字，并且实现较好的通用性（当send，more,money改变时，可以只改变ver的值实现修改）
，如果用数学知识，还可以推出部分字母的唯一可能取值（提高运行速度）（本程序默认均未知）并且在cor中用-1表示未知
'''
import time
start = time.time()

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def se(i, k, det, cor, carry, ver):  # 加法第二行的数字
    for j in nums:
        if det[j]:
            continue
        det[j] = 1
        cor[ver[k][1]] = j
        if cor[ver[k][2]] == -1:
            tem = (i+j+carry) % 10
            if det[tem]:
                det[j] = 0
                cor[ver[k][1]] = -1
                continue
            det[tem] = 1
            cor[ver[k][2]] = tem
            dfs(k-1, cor, det, (i+j)//10, ver)
            det[tem] = 0
            cor[ver[k][2]] = -1
        else:
            tem = cor[ver[k][0]]+cor[ver[k][1]]+carry
            if cor[ver[k][2]] == tem % 10:
                dfs(k-1, cor, det, tem//10, ver)
            else:
                det[j] = 0
                cor[ver[k][1]] = -1
                continue
        det[j] = 0
        cor[ver[k][1]] = -1
    return


def fi(k, det, cor, carry, ver):  # 加法第一行的数字
    for i in nums:
        if det[i]:
            continue
        det[i] = 1
        cor[ver[k][0]] = i
        if cor[ver[k][1]] == -1:
            se(i, k, det, cor, carry, ver)
        elif cor[ver[k][2]] == -1:
            tem = cor[ver[k][0]]+cor[ver[k][1]]+carry
            if det[tem % 10]:
                det[i] = 0
                cor[ver[k][0]] = -1
                continue
            else:
                det[tem % 10] = 1
                cor[ver[k][2]] = tem
                dfs(k-1, cor, det, tem//10, ver)
                det[tem % 10] = 0
                cor[ver[k][2]] = -1
        else:
            tem = cor[ver[k][0]]+cor[ver[k][1]]+carry
            if cor[ver[k][2]] == tem % 10:
                dfs(k-1, cor, det, tem//10, ver)
            else:
                det[i] = 0
                cor[ver[k][0]] = -1
                continue
        det[i] = 0
        cor[ver[k][0]] = -1
    return


def dfs(k, cor, det, carry, ver):
    if k == 0:
        if carry == cor[ver[k][2]] and cor[ver[k][2]] != 0:
            print(cor)
            return
    else:
        if cor[ver[k][0]] == -1:
            fi(k, det, cor, carry, ver)
        elif cor[ver[k][1]] == -1:
            se(cor[ver[k][0]], k, det, cor, carry, ver)
        elif cor[ver[k][2]] == -1:
            tem = cor[ver[k][0]]+cor[ver[k][1]]+carry
            if det[tem % 10]:
                return
            else:
                det[tem % 10] = 1
                cor[ver[k][2]] = tem
                dfs(k-1, cor, det, tem//10, ver)
                det[tem % 10] = 0
                cor[ver[k][2]] = -1
        else:
            tem = cor[ver[k][0]]+cor[ver[k][1]]+carry
            if cor[ver[k][2]] == tem % 10:
                dfs(k-1, cor, det, tem//10, ver)
            else:
                return


if __name__ == '__main__':
    det = [0]  # 判断某个数字是否被使用过
    det *= 10
    cor = {'M': -1, 'S': -1, 'O': -1, 'E': -1, 'N': -
           1, 'R': -1, 'D': -1, 'Y': -1}  # 字母与数值的对应
    ver = [['.', '.', 'M'], ['S', 'M', 'O'], ['E', 'O', 'N'],
           ['N', 'R', 'E'], ['D', 'E', 'Y']]  # 已知的加法关系
    dfs(4, cor, det, 0, ver)
    print(time.time()-start)
