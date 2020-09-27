def factorial(n):
    # 1! = 1
    if n == 1:
        return 1
    # n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


print(factorial(5))
