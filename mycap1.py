def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = fibonacci_recursive(n - 1)
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def fibonacci_nth_iterative(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

def fibonacci_nth_recursive(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci_nth_recursive(n - 1) + fibonacci_nth_recursive(n - 2)

# Example usage
n = 10
print(f"First {n} Fibonacci numbers (Iterative): {fibonacci_iterative(n)}")
print(f"First {n} Fibonacci numbers (Recursive): {fibonacci_recursive(n)}")
print(f"The {n}-th Fibonacci number (Iterative): {fibonacci_nth_iterative(n)}")
print(f"The {n}-th Fibonacci number (Recursive): {fibonacci_nth_recursive(n)}")

