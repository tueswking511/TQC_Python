srcfile = open('scores.dat', 'r')
line = srcfile.readline()
while line != '':
    print(line)
    line = srcfile.readline()
srcfile.close()
