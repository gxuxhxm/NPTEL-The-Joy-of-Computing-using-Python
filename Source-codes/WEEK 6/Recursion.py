# Recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Recursive Fibonacci function
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)