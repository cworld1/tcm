inputStr = str.lower(input('Please input a string: '))

# 逐个字符验证是否符合条件并提取到临时字符串上
vowels = ['a', 'e', 'i', 'o', 'u']
str = ''
step = 0
for letter in inputStr:
    step += 1
    if letter in vowels:
        str += letter
    if vowels[0] in str and vowels[1] in str and vowels[2] in str and vowels[3] in str and vowels[4] in str:
        break

# 对临时字符串去重处理
strList = list(str)
dealedList = list(set(strList))
dealedList.sort(key=strList.index)
if dealedList == []:
    print('Sorry. No vowel was found.')
else:
    print('These vowels were found: ' + ''.join(dealedList))
    print('Times we checked: ', step)
