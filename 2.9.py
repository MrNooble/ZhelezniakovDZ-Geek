a = input('Введи числа: ')
b = a.split(' ')
max = 0

for i in b[0]:
    max += int(i)
res = b[0]
sum = 0

print(f'максимальная сумма чисел {max} у числа {res}')