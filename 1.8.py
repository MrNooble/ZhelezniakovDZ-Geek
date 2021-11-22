year = int(input('Enter year: '))

if year % 400 or year % 4 == 0 and year % 100 != 0 == 0:
    print(True)
else:
    print(False)
