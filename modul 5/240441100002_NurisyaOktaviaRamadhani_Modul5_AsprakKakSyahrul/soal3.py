def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
angka = int(input("Masukkan angka untuk menghitung faktorialnya: "))
if angka < 0:
        print("Faktorial tidak terdefinisi untuk bilangan negatif.")
else:
    hasil = faktorial(angka)
    print(f"{angka}! = {hasil}")