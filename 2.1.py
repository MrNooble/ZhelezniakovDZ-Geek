def count(a, b, c,):
  match a, b, c:
    case int(a, b), с = '+':
      print(f"{a + b}")
    case int(a, b), с = '-':
      print(f"{a - b}")
    case int(a, b), с = '/':
      if b = 0:
        print("На ноль нельзя делить")
      else:
      print(f"{a / b}")
    case int(a, b), с = '*':
      print(f"{a * b}")
    case int(a, b), с = '0':
      print("Chao")
      exit(0)
    case _:
      print("Error")

    
while c!= '0':
  a = input('Первое число: ')
  b = input('Второе число: ')
  c = input('Знак операции: ')
  # c может быть + - / *. Для выхода введи значиние с = 0.
  if a.isdidit and b.isdigit:
    count(a, b, c)
  else:
    print(f'{a} и {b} число, дружище, ЧИСЛО!')
