def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

print(fib(3))