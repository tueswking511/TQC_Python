num = eval(input())
sum = 1

for i in range(1, num + 1):
    sum *= i
    print('#%2d! = %d' % (i, sum))
