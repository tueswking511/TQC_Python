desflie = open('scores.dat', 'w')
while True:
    s = input()
    n = input()
    if s == 'none':
        break
    desflie.write(s+' '+n+'\n')
desflie.close()
