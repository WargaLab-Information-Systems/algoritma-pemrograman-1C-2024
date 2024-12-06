def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n <= 0:
            print("Input tidak valid, masukkan bilangan non-negatif")
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Masukkan angka: "))
print(f"Bilangan fibonacci pada baris ke-{n} adalah {fibonacci(n)}")