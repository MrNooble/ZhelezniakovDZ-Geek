x1, y1 = int(input('Enter x1: ')), int(input('Enter y1'))
x2, y2 = int(input('Enter x2: ')), int(input('Enter y2: '))

k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
sig = '+' if b > 0 else '-'
print(f'y = {k} * x {sig} {abs(b)}')
