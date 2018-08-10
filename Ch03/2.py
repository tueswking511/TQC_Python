n = eval(input())
for i in range(1, n + 2):
    for j in range(1, i):
        print('%-4d' % j, end='')
    print()
