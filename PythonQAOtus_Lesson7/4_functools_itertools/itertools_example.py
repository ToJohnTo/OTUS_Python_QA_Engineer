import itertools

print(dir(itertools))

s = "abc"

res = itertools.cycle(s)

for el in res:
    print(el)

res = itertools.count(10, 2)

for el in res:
    print(el)

s = ['a', 'b', 'c']

res = itertools.combinations_with_replacement(s, r=3)

print(list(res))
