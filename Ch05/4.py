def totalAndmean():
    sum = 0
    for i in range(1, 11):
        sum += eval(input())
    return sum


def main():
    sum = totalAndmean()
    print('sum = %.2f, mean = %.2f' % (sum, sum / 10))


main()
