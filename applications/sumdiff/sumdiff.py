"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

from itertools import product
#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

cache = {}
for value in q:
    cache[value] = f(value)
result = []
combos = product(q,repeat=4)

for combo in combos:
    a = combo[0]
    b = combo[1]
    c = combo[2]
    d = combo[3]
    if cache[a] + cache[b] == cache[c] - cache[d]:
        result.append([a,b,c,d])


for combo in result:
    print(f'f({combo[0]}) + f({combo[1]}) = f({combo[2]}) - f({combo[3]})')



