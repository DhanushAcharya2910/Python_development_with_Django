def fibonacci_iterative(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series


n = int(input("enter the number"))
result = fibonacci_iterative(n)
print(f"The Fibonacci series up to {n} terms is: {result}")
