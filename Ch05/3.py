def BMI(h, w):
    bmi = w / pow(h * 0.01, 2)
    if bmi < 18.5:
        print('Your bmi is Under wright')
    elif 18.5 <= bmi < 25:
        print('Your bmi is Normal')
    elif 25.0 <= bmi < 30:
        print('Your bmi is Over weight')
    elif 30 <= bmi:
        print('Your bmi is fat')


def main():
    BMI(eval(input()), eval(input()))


main()
