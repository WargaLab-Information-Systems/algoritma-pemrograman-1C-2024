tahun = int(input("Masukkan tahun: "))

# Tahun kabisat jika habis dibagi 4, tetapi tidak habis dibagi 100, kecuali habis dibagi 400
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")