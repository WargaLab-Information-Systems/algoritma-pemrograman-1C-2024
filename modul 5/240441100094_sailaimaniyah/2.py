def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekurens fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Masukkan nilai n: "))
print("Bilangan Fibonacci ke-",n,"adalah",fibonacci(n))