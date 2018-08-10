lst = []
while True:
    s = input()
    if s == 'end':
        print(lst)
        break
    elif s.endswith('e'):
        lst.append(s)
