def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan nilai n: "))
print(f"{n}!= {faktorial(n)}")

while n > 1:
    print(f"{n} x ", end="")
    n-=1
print(n)    