def faktorial(n): 
    if n == 1 or n == 0:
        return 1
    elif n < 0 :
        print("Input tidak valid")
    else :
        return n * faktorial(n - 1)
n = int(input("Masukkan angka: "))
print(n, "! = ", end='')
faktorial(n)
print("Cara menghitungnya : ", end='')
while n > 1:
    print(f"{n} x ", end="")
    n -= 1
print("1")