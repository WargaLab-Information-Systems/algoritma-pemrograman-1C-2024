def hitung_faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."
    elif n == 0 or n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(2, n + 1):
            faktorial *= i
        return faktorial

bilangan = int(input("Masukkan sebuah bilangan bulat non-negatif: "))
hasil = hitung_faktorial(bilangan)
print(f"{bilangan}! = {hasil}")
