def fibonacci(n):
    # Memeriksa apakah n adalah 0 atau 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Memanggil fungsi fibonacci secara rekursif
        # bilangan yang dikurangi 1 dan 2 dari parameter 
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan
while True:
    n = int(input("Masukkan bilangan bulat non-negatif n: "))
    if n < 0:
        print("Silakan masukkan bilangan bulat non-negatif.")
    else:
        print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")
        break
