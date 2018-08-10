import random

lst = []
set = set()
for i in range(10):
    lst.append(random.randint(1, 100))
    set.add(lst[i])
print(lst)
print(set)
