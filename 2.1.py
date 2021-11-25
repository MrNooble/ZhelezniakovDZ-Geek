def count(user_input: list):
  match user_input:
    case int(a, b), '+':
      print(f"{a + b}")
    case int(a, b), '-':
      print(f"{a - b}")
    case int(a, b), '/': 
      print(f"{a / b}")
    case int(a, b), '*':
      print(f"{a * b}")
    case _:
      print('Error')
      exit(0)
