a = input('Enter your number: ')
b = 0
c = 1
match list(a):
    case a1, a2, a3:
        print(int(a1) + int(a2) + int(a3))
        print(int(a1) * int(a2) * int(a3))
    case _:
        print('error')
