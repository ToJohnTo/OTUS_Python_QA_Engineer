def is_digit(x):
    return str(x).isnumeric()


s = [None, [], "2", 2, -1.0, int, str]

filtered_s = filter(is_digit, s)

print(list(filtered_s))
