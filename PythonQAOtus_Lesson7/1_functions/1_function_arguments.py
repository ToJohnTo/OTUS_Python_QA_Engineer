def foo(a, b=1):
    return a + b


def any_args(*args):
    print(args)


any_args(1, 2, 3, 4)


def any_kwargs(**kwargs):
    print(kwargs)


any_kwargs(test=1, money=2)


def any_of_any(*args, **kwargs):
    print(args)
    print(kwargs)


any_of_any(1, 2, 3, 4, test=1, money=2)
