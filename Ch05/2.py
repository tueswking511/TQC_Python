def GPA(score):
    if 100 >= score >= 90:
        print('A')
    elif 89 >= score >= 80:
        print('B')
    elif 79 >= score >= 70:
        print('C')
    elif 69 >= score >= 60:
        print('D')
    elif 59 >= score:
        print('E')


def main():
    GPA(eval(input()))


main()
