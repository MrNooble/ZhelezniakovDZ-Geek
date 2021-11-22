a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

a, b, c = sorted([a, b, c])
print(f'min {a}, midle {b}, max {c}')
