# Meminta input dari pengguna
angka = input("Masukkan angka yang akan dibalik : ")

# Inisialisasi variabel untuk menyimpan angka terbalik
angka_terbalik = ""
i = 0

# Menggunakan perulangan while untuk membalikkan urutan
while angka[i:i+1]:  # Memeriksa apakah karakter ada yang perlu dibalik
    angka_terbalik = angka[i] + angka_terbalik
    i += 1

# Menampilkan hasil
print("Angka setelah dibalik:", angka_terbalik)
