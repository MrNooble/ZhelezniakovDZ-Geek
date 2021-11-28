from random import randint, seed

seed(20)
init_list = [randint(0, 100) for i in range(10)]
y = [k for k, t in enumerate(init_list) if t % 2 == 0]

print(init_list, y)
