import inspect

fun_lambda = lambda x, y: x ** 2 + y ** 2

print(fun_lambda(2, 2))


def fun():
    print('_function_')


def fun_return():
    return '_function_'


# ? ? ?
# print(fun())

print('# ' * 30)

print(type(fun))

print(dir(fun))

print(fun.__name__)

print(fun.__code__)

print(inspect.getsource(fun))

print('# ' * 30)

list_of_functions = [fun, fun, fun]

print(list_of_functions)

for f in list_of_functions:
    f()

print('# ' * 30)

a = fun

a()

print('# ' * 30)


def foo(f): return f


foo(foo(fun))()

print('# ' * 30)
