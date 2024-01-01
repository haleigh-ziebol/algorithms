def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
   
# Example usage
n = 20  # Change this value to compute a different term in the sequence
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

# Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Example usage
n = 10  # Change this value to compute a different term in the sequence
print(f"The {n}th Fibonacci number is: {fibonacci_memo(n)}")

# Tabulation
def fibonacci_tab(n):
    if n <= 1:
        return n

    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

# Example usage
n = 10  # Change this value to compute a different term in the sequence
print(f"The {n}th Fibonacci number is: {fibonacci_tab(n)}")



