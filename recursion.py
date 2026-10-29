def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)