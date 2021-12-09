from memory_profiler import profile


@profile
def get_simple(index, simples=[], iteration=1, step=1000):
    n = iteration * step
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    if len(b) < index:
        return get_simple(index, b, iteration + 1, step)
    else:
        return b[index - 1]


get_simple(5)

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10     14.7 MiB     14.7 MiB   @profile
#     11                             def get_simple(index, simples=[], iteration=1, step=1000):
#     12     14.7 MiB      0.0 MiB       n = iteration * step
#     13     14.7 MiB      0.0 MiB       a = [0] * n  # создание массива с n количеством элементов
#     14     14.7 MiB      0.0 MiB       for i in range(n):  # заполнение массива ...
#     15     14.7 MiB      0.0 MiB           a[i] = i  # значениями от 0 до n-1
#     16
#     17                                 # вторым элементом является единица, которую не считают простым числом
#     18                                 # забиваем ее нулем.
#     19     14.7 MiB      0.0 MiB       a[1] = 0
#     20
#     21     14.7 MiB      0.0 MiB       m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
#     22     14.7 MiB      0.0 MiB       while m < n:  # перебор всех элементов до заданного числа
#     23     14.7 MiB      0.0 MiB           if a[m] != 0:  # если он не равен нулю, то
#     24     14.7 MiB      0.0 MiB               j = m * 2  # увеличить в два раза (текущий элемент простое число)
#     25     14.7 MiB      0.0 MiB               while j < n:
#     26     14.7 MiB      0.0 MiB                   a[j] = 0  # заменить на 0
#     27     14.7 MiB      0.0 MiB                   j = j + m  # перейти в позицию на m больше
#     28     14.7 MiB      0.0 MiB           m += 1
#     29
#     30                                 # вывод простых чисел на экран (может быть реализован как угодно)
#     31     14.7 MiB      0.0 MiB       b = []
#     32     14.7 MiB      0.0 MiB       for i in a:
#     33     14.7 MiB      0.0 MiB           if a[i] != 0:
#     34     14.7 MiB      0.0 MiB               b.append(a[i])
#     35
#     36     14.7 MiB      0.0 MiB       if len(b) < index:
#     37                                     return get_simple(index, b, iteration+1, step)
#     38                                 else:
#     39     14.7 MiB      0.0 MiB           return b[index-1]
