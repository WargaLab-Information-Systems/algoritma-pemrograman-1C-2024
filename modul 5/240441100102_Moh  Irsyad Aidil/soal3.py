def faktorial(n):
    # Basis kasus
    if n == 0 :
        return 1
    elif n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan nilai n: "))
print(f"{n}! = {faktorial(n)}")
for i in range(1, n + 1):
    print(i, end= " ")


