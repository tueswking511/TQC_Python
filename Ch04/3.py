start = eval(input())
end = eval(input())
for i in range(start, end + 1):
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        print('%d ' % i, end='')
