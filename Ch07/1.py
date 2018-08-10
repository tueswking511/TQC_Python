import random

lst = []
tuple = ()
for i in range(10):
    lst.append(random.randint(1, 100))
    tuple += (lst[i],)
print(lst)
print(tuple)
