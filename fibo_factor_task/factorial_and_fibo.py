def factorial(n: int) -> int :
    if n<0:
        raise ValueError("Факториал определен только для неотрицательных")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n<0:
        raise ValueError("Факториал определен только для неотрицательных")

    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1)

def fibo(n: int) -> int:
    if n<0:
        raise ValueError("Числа Фибоначчи определены только для неотрицательных")

    if n==0: return 0
    if n==1: return 1

    a = 0
    b = 1
    for i in range(2, n+1):
        a, b =  b, a+b
    return b

def fibo_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Числа Фибоначчи определены только для неотрицательных")

    if n == 0: return 0
    if n == 1: return 1

    return fibo_recursive(n-1)+fibo_recursive(n-2)


