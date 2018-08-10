def inputData(lst35):
    for i in range(3):
        print('#%d student' % (i + 1))
        lst35.append([])
        for j in range(5):
            lst35[i].insert(j, eval(input()))
    return lst35


def totAver(lst35):
    for i in range(len(lst35)):
        print('#%d student:' % (i + 1))
        print('sum = %d, average = %.2f' % (sum(lst35[i]), sum(lst35[i]) / len(lst35[i])))
        print()


def main():
    lst35 = []
    lst35 = inputData(lst35)
    totAver(lst35)


main()
