def inputData(set10):
    while True:
        a = eval(input())
        if a != -9999:
            set10.add(a)
        else:
            break
    return set10


def operation(set11,set12):
    print('set1 is a subset of set2: ',set11.issubset(set12))
    print('set1 is a superset of set2: ', set11.issuperset(set12))


def main():
    print('Input set1 data: ')
    set1 = set()
    inputData(set1)

    print('Input set1 data: ')
    set2 = set()
    inputData(set2)

    print('set1',set1)
    print('set2',set2)
    operation(set1, set2)


main()
