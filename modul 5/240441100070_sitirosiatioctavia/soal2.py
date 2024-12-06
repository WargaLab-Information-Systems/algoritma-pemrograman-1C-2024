def fibonacci(n):
    # Basis: jika n adalah 0 atau 1, langsung mengembalikan n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekursi: menghitung bilangan Fibonacci ke-n dengan memanggil fibonacci(n-1) dan fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Meminta input dari pengguna
n = int(input("Masukkan nilai n: "))
print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")
