def faktorial(n):
    # Basis: jika n adalah 0 atau 1, kembalikan 1 (0! = 1 dan 1! = 1)
    if n == 0 or n == 1:
        return 1
    # Rekurens: hitung n * faktorial(n - 1)
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
print(f"{n}! = {faktorial(n)}")
