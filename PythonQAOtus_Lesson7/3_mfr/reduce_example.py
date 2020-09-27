import functools


def foo(x, y):
    print(x, " * ", y)
    return x * y


r = range(1, 5)

res = functools.reduce(foo, r)

print(res)
