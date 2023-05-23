# count é um iterador sem fim (itertools)
# (não fala quando acaba igual no range)

from itertools import count

c1 = count()
print(next(c1))
print(next(c1))

for i in c1:
    if i > 100:
        break
    print(i)