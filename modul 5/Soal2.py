def fibonacci(n):
    # Basis kasus
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekurens
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan nilai n: "))
print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")

# 0 1 1 2 3 5 8 13 21