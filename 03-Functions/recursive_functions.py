# A recursive function is a function that calls itself. It's useful for problems that can be broken into smaller subproblems (e.g., factorial, Fibonacci).

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
