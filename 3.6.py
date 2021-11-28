from random import randint

fl = [randint(-10, 30) for _ in range(12)]
fp, lp = fl.index(min(fl)), fl.index(max(fl))
settings = 1 if lp > fp else -1
print(fl)
print(sum(fl[fp:lp:settings]) - fl[fp])
