import random as rn


def get_median(ls: list):
    avg = sum(ls)/2  # среднее
    med_i = 0
    min_delta = float('inf')

    for i, x in enumerate(ls):
        delta = abs(x-avg)
        if min_delta > delta:
            min_delta = delta
            med_i = i

    return ls[i]


ls = [rn.randint(-10, 10) for x in range(11)]
print(ls)
print('Медиана:', get_median(ls))