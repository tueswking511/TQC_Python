num = eval(input('Enter a number: '))
i = 2
while True:
    if num % i == 0:
        print('The smallest factor is %d' % i)
        break
    else:
        i += 1
