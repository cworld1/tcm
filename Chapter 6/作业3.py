from copy import deepcopy

# (a) changing x also changes y
x = [1, 2, 3]  # 已给出
y = []
y = x

x[0] = 0
print(y)

# (b) changing x does not change y
x = [1, 2, 3]  # 已给出
y = []
y = deepcopy(x)

x[0] = 0
print(y)
