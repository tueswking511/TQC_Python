dic = {}
while True:
    print('1: add')
    print('2: delete')
    print('3: query')
    print('4: display')
    print('5: exit')
    type = eval(input('Which one: '))
    if type == 1:
        key = eval(input('Input key: '))
        value = input('Input value: ')
        dic[key] = value
    elif type == 2:
        key = eval(input('Input key: '))
        if key in dic:
            del dic[key]
            print('%d has been deleted' % key)
        else:
            print('not found')
    elif type == 3:
        key = eval(input('Input key: '))
        print(dic[key])
    elif type == 4:
        for key in dic:
            print('%s:%s' % (key, dic[key]))
    elif type == 5:
        break
    else:
        continue
    print()
