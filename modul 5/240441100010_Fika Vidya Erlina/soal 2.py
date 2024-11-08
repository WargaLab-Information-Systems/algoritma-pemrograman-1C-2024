def fibonacci(n):
    if n == 0 or n == 1:
        return n
    # Rekurens
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Program utama untuk menampilkan deret Fibonacci hingga n
n = int(input("Masukkan nilai n: "))
print("Deret Fibonacci hingga ke-", n, ":")
for i in range(n + 1):
    print(fibonacci(i), end=" ")