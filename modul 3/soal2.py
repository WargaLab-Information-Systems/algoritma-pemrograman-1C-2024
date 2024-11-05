# input dari pengguna
angka_input = input("Masukkan angka bulat: ")

# membalikkan urutan angka menggunakan loop
angka_balik = ""
for i in angka_input:
    angka_balik = i + angka_balik  # tambahkan digit di depan

# hasil
print("Angka setelah dibalik:", angka_balik)