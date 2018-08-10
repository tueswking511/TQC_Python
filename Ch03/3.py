a = eval(input())
b = eval(input())
sum = 0
for i in range(a, b + 1):
    sum += i if i % 2 == 0 else 0
print('total = %d' % sum)
