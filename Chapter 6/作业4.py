L = [1, 2, 3, 4]  # 已给出

# 给出示例
# string = ''.join([i for i in L])

# 修复示例（将返回值中的int类型转化为str类型）
string = ''.join([str(i) for i in L])
print(string)
