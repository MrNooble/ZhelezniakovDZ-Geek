from random import randint

P = 4
matr = [[randint(0, 10) for _ in range(P)] for _ in range(P)]
for i in matr:
    i += [sum(i)]
str_fin = '\n'.join(['\t'.join(map(str, i)) for i in matr])
print(str_fin)
print(matr)
