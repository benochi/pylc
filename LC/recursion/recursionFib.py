# fibonacci f(number) = f(n-1) + f(n-2)
# #recursive(not efficient)


def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci((number - 1)) + fibonacci(number - 2)


print(fibonacci(20))
