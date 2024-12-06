def fibonacci(n):
    # Basis kasus
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekurens
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))
print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")