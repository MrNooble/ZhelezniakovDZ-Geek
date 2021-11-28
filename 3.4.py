from collections import Counter
from random import randint

init_list = [randint(0, 10) for _ in range(10)]
print(init_list)
print(Counter(init_list).most_common(1))
