tahun = int(input("Masukkan tahun: "))

# Tahun kabisat jika habis dibagi 4, 
# tetapi jika dapat dibagi 100, maka tahun itu tidak kabisat kecuali juga dapat dibagi 400

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")