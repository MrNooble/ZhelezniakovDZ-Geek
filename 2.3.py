a = input('Число: ')

def rev(a):
  if a.isdigit():
    fin = a[::-1]
    return print(fin)
  else:
    print('Только числа')
    exit(0)
    
    
 rev(a)
