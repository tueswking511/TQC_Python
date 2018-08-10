x = 1
y = 1

while x < 10:
    while y < 10:
        print('%d*%d=%2d ' % (x, y, x * y), end=' ')
        y += 1
    print()
    x += 1
    y = 1
