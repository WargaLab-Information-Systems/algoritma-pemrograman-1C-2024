def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Masukkan nilai n untuk menghitung bilangan Fibonacci ke-n: "))
if n < 0:
        print("Input tidak valid. Harap masukkan bilangan bulat non-negatif.")
else:
        hasil = fibonacci(n)
        print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")