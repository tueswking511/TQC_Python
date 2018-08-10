lst = []
for i in range(10):
    s = input()
    lst.append(s)
for i in range(0, len(lst)-1, 3):
    print('|%s||%s||%s|' % (lst[i].ljust(15), lst[i + 1].ljust(15), lst[i + 2].ljust(15)))
