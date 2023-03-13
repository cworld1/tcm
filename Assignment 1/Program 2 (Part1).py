A, B = 34, 19
product = 0

while B:
    if B % 2:
        product += A
    A *= 2
    B //= 2
print('The product of two integers is:', product)
