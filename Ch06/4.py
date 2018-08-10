def meanAndsd(Lst):
    mean = sum(Lst) / len(Lst)
    sd = 0
    for i in range(len(Lst)):
        sd = pow(Lst[i] - mean, 2)
    sd = pow(sd / len(Lst), 1 / 2)
    print('mean = %.2f, standard deviation = %.2f' % (mean, sd))


def main():
    Lst = []
    for i in range(10):
        Lst.append(eval(input()))
    meanAndsd(Lst)


main()
