def compute(a, b):
    Lst = []
    for i in range(a, b + 1):
        num = i
        n = len(str(i))
        sum = 0
        while num > 0:
            sum += pow(num % 10, n)
            sum = int(sum)
            num = int(num/10)
        if sum == i:
            Lst.append(i)
    return Lst


Lst = []
Lst = compute(eval(input()), eval(input()))
for i in range(len(Lst)):
    print('%d ' % (Lst[i]), end='')
