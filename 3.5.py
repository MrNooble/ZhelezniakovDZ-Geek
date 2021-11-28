from random import randint

first_list = [randint(-10, 10) for _ in range(10)]
print(first_list)
val = max(list(filter(lambda x: x < 0, first_list)))
print(f'Max value {val} on position {first_list.index(val)}')
