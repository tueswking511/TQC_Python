s = input()
for i in range(len(s)):
    if s[i].isupper():
        print('%s: is upper alpha.' % (s[i]))
    elif s[i].islower():
        print('%s: is lower alpha.' % (s[i]))
    elif s[i].isspace():
        print('%s: is space.' % (s[i]))
    else:
        print('%s is a symbol character.' % (s[i]))
