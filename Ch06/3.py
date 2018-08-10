import random


def maxAndmin(randLst):
    print(randLst[1])
    print(randLst[len(randLst) - 2])


randLst = []
while len(randLst) < 100:
    num = random.randint(1, 1000)
    if num not in randLst:
        randLst.append(num)
randLst.sort()
for i in range(len(randLst)):
    if (i + 1) % 10 == 0:
        print('%4d' % (randLst[i]))
    else:
        print('%4d' % (randLst[i]), end='')
print()
maxAndmin(randLst)
