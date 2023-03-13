for i in range(0, 20, 2):
    count, str = 0, '*'
    while count < i:
        str = str + ' *'
        count += 1
    print('{:^40s}'.format(str))
