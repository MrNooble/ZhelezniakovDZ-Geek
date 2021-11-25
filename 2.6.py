import random

a = random.randint(0, 100)
b = int(input('Угадайка чило от 1 до 100: '))
i = 10

while i != 0:
    if a == b:
        print('БИНГО')
        exit(0)
    elif a > b:
        print(f'Больше {b}')
        i -= 1
    else:
        print(f'Меньше {b}')
        i -= 1
        b = int(input(f'У вас осталось {i} попыток, введите число: '))

print(f'Вы проиграли, число было {a}')