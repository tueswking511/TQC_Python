num = [0, 0, 0, 0]
for i in range(1, 11):
    print('1: Peter')
    print('2: Nancy')
    print('3: Mary')
    sel = eval(input('Which one do you prefer: '))
    if 1 <= sel <= 3:
        num[sel - 1] += 1
    else:
        num[3] += 1
    print('Peter: %d, Nancy: %d, Mary: %d' % (num[0], num[1], num[2]))
print()
print('Peter: %d, Nancy: %d, Mary: %d' % (num[0], num[1], num[2]))
print('Invalid: %d' % num[3])
