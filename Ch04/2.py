n1 = eval(input('Enter a number1:'))
n2 = eval(input('Enter a number2:'))
i = 1
ans = 1
while True:
    if i == n1 or i == n2:
        print('The greatest common factor is %d' % ans)
        break
    elif n1 % i == 0 and n2 % i == 0:
        ans = i
    i += 1
