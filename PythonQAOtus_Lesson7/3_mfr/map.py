def foo(x):
    return x ** 0.5


def foo2(x):
    return int(x ** 2)


s = range(10)

res = map(foo, s)
res = map(foo2, res)

print(list(res))
