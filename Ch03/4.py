num = eval(input('Enter a number: '))
for i in range(num, 0, -1):
    for j in range(1, i+1):
        print('%-4d' % j, end='')
    print()
