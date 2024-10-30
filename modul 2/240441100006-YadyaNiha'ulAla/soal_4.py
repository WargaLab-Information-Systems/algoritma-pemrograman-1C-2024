tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")

# Aturan: harus habis dibagi 4, 
# tetapi tidak boleh habis dibagi 100, 
# kecuali jika juga habis dibagi 400.

