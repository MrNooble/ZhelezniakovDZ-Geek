def bubble_sort(ls: list, asc=False) -> list:
    ls_len = len(ls)
    j = 1
    k = 1 if asc else -1

    while j < ls_len:
        for i in range(ls_len-j):
            if k*ls[i] < k*ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
        j += 1

    return ls


ls = [rn.randint(-100, 100) for x in range(10)]
print(ls, '->')
print('desc', bubble_sort(ls))
print('asc', bubble_sort(ls, asc=True))