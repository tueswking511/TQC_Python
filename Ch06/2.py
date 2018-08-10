def show(list1, list2, sum):
    print('Matrix 1')
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            print('%3d' % (list1[i][j]), end='')
        print()
    print('Matrix 2')
    for i in range(len(list2)):
        for j in range(len(list2[0])):
            print('%3d' % (list2[i][j]), end='')
        print()
    print('Sum of matrices')
    for i in range(len(sum)):
        for j in range(len(sum[0])):
            print('%3d' % (sum[i][j]), end='')
        print()


def multiply(list1, list2):
    sum = []
    for i in range(2):
        sum.append([])
        for j in range(2):
            calu = 0
            for k in range(2):
                calu = calu + list1[i][k] * list2[k][j]
            sum[i].insert(j, calu)
    return sum


def main():
    list1 = []
    list2 = []
    print('Enter matrix1:')
    for i in range(2):
        list1.append([])
        for j in range(2):
            list1[i].append(eval(input('[%d %d]: ' % (i + 1, j + 1))))
    print('Enter matrix2:')
    for i in range(2):
        list2.append([])
        for j in range(2):
            list2[i].append(eval(input('[%d %d]: ' % (i + 1, j + 1))))
    show(list1, list2, multiply(list1, list2))


main()
