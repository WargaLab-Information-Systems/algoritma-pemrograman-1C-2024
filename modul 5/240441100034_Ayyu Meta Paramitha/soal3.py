n = int(input("angka faktorial : "))

def faktorial(n):
    # Memeriksa kasus dasar
    if n == 0:
        return 1
    else:
        # Menggunakan rekursi untuk menghitung faktorial
        return n * faktorial(n - 1)

print(f"Faktorial dari n : {faktorial(n)}")
 