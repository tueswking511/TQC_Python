dict10 = {}

while True:
    print('Input key: ', end='')
    k = eval(input())
    print('Input value: ', end='')
    v = input()
    if k != -9999:
        dict10[k] = v
    else:
        break
print(dict10)
k = eval(input('What key do you want to delete: '))
if k in dict10:
    del dict10[k]
    print(dict10)
else:
    print('not found')
