srcfile = open('scores.dat', 'r')
line = srcfile.readline()
score = 0
count = 0
while line != '':
    lst = line.split(' ')
    score += int(lst[1])
    count += 1
    line = srcfile.readline()
srcfile.close()
print('average score : %.2f' % (score/count))
