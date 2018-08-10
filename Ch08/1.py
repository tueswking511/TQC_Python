while True:
    strinput = input()
    if strinput == 'end':
        break
    else:
        lst = strinput.split(':')
        print('hour: %s, min: %s, second: %s' % (lst[0], lst[1], lst[2]))
