# Meminta input angka dari pengguna
angka = input("Masukkan angka: ")

# Membalikkan urutan angka menggunakan perulangan
angka_terbalik = ""
for digit in angka:
    angka_terbalik = digit + angka_terbalik  # Menambahkan digit di depan hasil sementara

# Menampilkan hasil
print("angka terbalik:" ,angka_terbalik)