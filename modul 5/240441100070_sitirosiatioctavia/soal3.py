def faktorial(n):
    # Basis: jika n adalah 0 atau 1, faktorialnya adalah 1
    if n == 0 or n == 1:
        return 1
    # Rekursi: menghitung faktorial dengan memanggil faktorial(n-1)
    else:
        return n * faktorial(n - 1)

# Meminta input dari pengguna
n = int(input("Masukkan bilangan: "))
print(f"{n}! = {faktorial(n)}")