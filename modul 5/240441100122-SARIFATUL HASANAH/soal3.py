def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    n = int(input("Masukkan bilangan bulat non-negatif untuk menghitung faktorial: "))

    if n < 0:
        print("Silakan masukkan bilangan bulat non-negatif.")
    else:
        
            
        print(f"{n}! = {faktorial(n)}")

        for i in range(1, n+1,):
            print(i, " ", end="")
        break

