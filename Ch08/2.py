while True:
    s = input()
    if s == '-1':
        break
    elif not s[0].isalpha():
        print('Invalid variable name')
        continue
    elif not s.isalnum():
        print('Invalid variable name')
        continue
    else:
        print('Valid variable name')
        continue
