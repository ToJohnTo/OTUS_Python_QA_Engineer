import functools
import timeit

print(dir(functools))


@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(timeit.timeit(lambda: fib(25), number=1000))


def foo(a, b, c):
    return a + b + c


res = functools.partial(foo, 5, 5)

print(res(5))
