def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case: Fib(n) = Fib(n-1) + Fib(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

# Test the function
print("Fibonacci sequence:")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")