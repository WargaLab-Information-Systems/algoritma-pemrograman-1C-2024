# program membalikkan urutan nilai
# program untuk meminta angka bulat
# variabel angka dengan input tipe data integer
angka = int(input("Masukkan angka bulat: "))

# variabel angka_terbalik diberikan nilai 0
angka_terbalik = 0

while angka != 0:

    digit = angka % 10

    angka_terbalik = angka_terbalik * 10 + digit

    angka = angka // 10

# menentukan hasil
print("Angka setelah dibalik:", angka_terbalik)
