srcfile = open('friends.dat', 'r')
for i in range(5):
    print(srcfile.readline())
srcfile.close()