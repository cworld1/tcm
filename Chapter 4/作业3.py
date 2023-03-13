import random

word = input('Please input a word: ')
if word.isalpha():
    # 创建单词序列并改变顺序
    order = list(word[1:-1])
    random.shuffle(order)
    print('The scrambled version: ' + word[0] + ''.join(order) + word[-1])
else:
    print('Sorry. What you input is incorrect.')
