def printStar():
    for i in range(1, 73):
        print('*', end='')
    print()


def multiply99():
    for i in range(1, 10):
        for j in range(1, 10):
            print('%d*%d=%2d  ' % (j, i, i * j), end='')
        print()


printStar()
multiply99()
printStar()
