a = input('Число: ')
even = 0
odd = 0

for i in a:
  if i.isdigit():
    if int(i) % 2 == 0:
      even +=1
    else:
      odd += 1
  else:
    print('ЧИСЛО!')
    exit(0)
    
print(f'в числе {a} {even} четных и {odd} нечетных')
