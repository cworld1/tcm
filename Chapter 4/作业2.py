# 判断是否含有数字
def checkNumber(str):
    for x in str:
        if x.isdigit():
            return True
    return False


# 判断是否同时含有大小写字母
def checkLetter(str):
    tag1 = tag2 = False
    for x in str:
        if x.isupper():
            tag1 = True
        if x.islower():
            tag2 = True
    return tag1 and tag2


password = input("请输入密码：")
# 规则1：密码长度
secure1 = len(password) in range(6, 21)
# 规则2：包含数字
secure2 = checkNumber(password)
# 规则3：包含大小写字母
secure3 = checkLetter(password)

if secure1 and secure2 and secure3:
    confirm = input("您的密码强度合格！是否确认使用该密码(Y/N): ")
    if confirm == 'Y':
        print('已成功使用该密码！')
    elif confirm == 'N':
        print('密码设置已取消！')
    else:
        print('未输入 Y/N 。已取消设置密码。')
else:
    print("您设置的密码强度不合格。请遵从以下规范：")
    if not secure1:
        print(" - 密码长度应不小于6位且不大于20位")
    if not secure2:
        print(" - 密码中应包含数字")
    if not secure3:
        print(" - 密码中应同时包含大小写字母")
