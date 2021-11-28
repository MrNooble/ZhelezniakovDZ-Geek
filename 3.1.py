first_list = [i for i in range(2, 100)]
for y in range(2, 10):
    print(f'{y} - {len(list(filter(lambda x: x % y == 0, first_list)))}')
