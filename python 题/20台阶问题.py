fib = lambda n: n if n <= 2 else fib(n-1) + fib(n-2)

def fib1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

print(fib1(3))