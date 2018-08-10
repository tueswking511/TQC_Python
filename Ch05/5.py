import re


def distance(x1, y1, x2, y2):
    print('The distance of ((%f, %f), (%f, %f)) = %.2f'
          % (x1, y1, x2, y2, pow(pow(x2 - x1, 2) + pow(y2 - y1, 2), 1 / 2)))


def main():
    x1 = y1 = x2 = y2 = 0
    string = eval(input())
    print(string[1])

    distance(x1, y1, x2, y2)


main()
