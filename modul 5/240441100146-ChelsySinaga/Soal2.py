n = int(input("masukkan nilai n :"))


def fibonacci(n):
    # Basis kasus: jika n adalah 0 atau 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekursi untuk menghitung fibonacci(n)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan fungsi
result = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah: {result}")
