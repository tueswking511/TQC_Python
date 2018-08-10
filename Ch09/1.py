desfile = open('friends.dat', 'w')
lst = []
for i in range(5):
    s = input()
    desfile.write(s+'\n')
desfile.close()
