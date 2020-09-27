def make_cool(foo):
    def wrapper():
        return "---= " + str(foo()) + " =---"

    return wrapper


@make_cool
def say_hello():
    return "hello"


print(say_hello())
