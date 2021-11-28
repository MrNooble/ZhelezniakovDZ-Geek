from random import randint

fl = [randint(-10, 15) for _ in range(11)]
sort = sorted(fl)
print(fl)
print(sort[0], sort[1])
