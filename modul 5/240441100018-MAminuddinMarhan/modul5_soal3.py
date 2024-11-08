def faktorial(z):
    if z == 0 or z == 1:
        return 1
    elif z < 0:
        print("Input tidak boleh negatif")
    else:
        return z * faktorial(z - 1)
z = int(input("Masukkan angka: "))
print(z,"! = ", end='')
print(faktorial(z))
print("Caranya adalah: ", end='')
while z > 1:
    print(f"{z} x ", end="")
    z -= 1
print("1")