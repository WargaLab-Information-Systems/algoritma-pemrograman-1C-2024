def faktorial(n):
    # basis kasus
    if n == 0 or n == 1:
        return 1
    # rekurens
    else:
        return n * faktorial(n-1)

n = int(input("masukkan nilai n: "))
print(f"{n}!= {faktorial(n)}")
for i in range(1, n + 1):
    print(i, end= "  ")