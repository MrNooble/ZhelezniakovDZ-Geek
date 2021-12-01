simples_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]


def get_simple(index, simples=[], iteration=1, step=1000):
    """
    Эмпирические данные:
    https://pastenow.ru/7400e49939ee65ae943eedafde2d2aec
    """

    n = iteration * step
    a = [0] * n
    for i in range(n):
        a[i] = i


    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1


    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    if len(b) < index:
        return get_simple(index, b, iteration + 1, step)
    else:
        return b[index - 1]


def test():
    method_res = get_simple(10)
    test_res = simples_test[9]

    print('Test passed' if method_res == test_res else 'Test failed')


def test_performance():
    from timeit import timeit

    def test_iteration(n):
        res = timeit(f'get_simple({n})', number=10,
                     setup='from __main__ import get_simple')
        print('N=', n, 'time=', res / 100)

    for x in [2 ** i for i in range(14)]:
        test_iteration(x)


if __name__ == '__main__':
    test()
    test_performance()