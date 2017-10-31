fib = lambda n: n if n < 2 else fib(n - 1) * 2

n = int(input('>>'))
print(fib(n))

print(2**(n-1))