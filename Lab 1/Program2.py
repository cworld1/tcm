for x in range(1, 10):
    for y in range(1, x+1):
        print('{}*{}={:<4}'.format(x, y, x*y), end='')
        print('\n')
