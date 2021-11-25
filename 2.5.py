start = 32
fin = 127
res = ''
i = 0
symbol = start
while symbol <= fin:
    res = res + chr(symbol) + ' - ' + str(symbol) + ','
    if (i + 1) % 10 == 0:
        res = res + '\n'
    i +=1
    symbol +=1

print(res)
