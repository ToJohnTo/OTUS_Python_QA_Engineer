def mul(times):
    def wrapper(x):
        print("{times} times {x} is".format(times=times, x=x), end=" ")
        return times * x

    return wrapper


ten_times = mul(10)

print(ten_times(2))
print(ten_times(3))

five_times = mul(5)

print(five_times(2))
print(five_times(3))
