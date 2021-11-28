from random import randint

first_list = [randint(0, 100) for _ in range(10)]
print(first_list)
first_list[first_list.index(max(first_list))], first_list[first_list.index(min(first_list))] = (
    first_list[first_list.index(min(first_list))], first_list[first_list.index(max(first_list))])
print(first_list)
