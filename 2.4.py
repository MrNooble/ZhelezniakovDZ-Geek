n = input('Колличество элементов: ')
i = 1
s = 1
if n.isdigit():
    n = int(n)
    if n > 0:
        while n > 0:
        i /= -2
        s += i
        n -= 1
    else:
        print('Введи ЧИСЛО, оно должно быть больше 1')
        exit(0)
else:
    print('Введи ЧИСЛО, оно должно быть больше 1')
    exit(0)

print(s)