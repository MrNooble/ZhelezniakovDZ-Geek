a = int(input('Enter 1st side: '))
b = int(input('Enter 2nd side: '))
c = int(input('Enter 3rd side: '))

if (a + b > c and a + c > b and b + c > a):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('Равнобедренный')
    elif a == c == b:
        print('Равносторонний')
    else:
        print('Разносторонний')
else:
    print('Перемудрил')
