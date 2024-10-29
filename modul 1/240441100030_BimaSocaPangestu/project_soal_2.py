# Diketahui
suku_ke_5 = 11
suku_ke_8_plus_suku_ke_12 = 52

# Misalkan:
# a = suku pertama
# d = beda deret

# Suku ke-5: a + 4d = 11
# Suku ke-8: a + 7d
# Suku ke-12: a + 11d

# Persamaan dari informasi yang diberikan
# (a + 7d) + (a + 11d) = 52
# 2a + 18d = 52

# Kita punya dua persamaan:
# 1. a + 4d = 11
# 2. 2a + 18d = 52

# Mengubah persamaan pertama untuk mendapatkan a
# a = 11 - 4d

# Substitusi a ke dalam persamaan kedua
# 2(11 - 4d) + 18d = 52
# 22 - 8d + 18d = 52
# 10d = 30
# d = 3

d = 3
a = 11 - 4 * d  # Menghitung a

# Hitung jumlah 8 suku pertama
jumlah_suku_pertama_8 = (8 / 2) * (2 * a + (8 - 1) * d)

# Menampilkan hasil
print(f"Suku pertama (a): {a}")
print(f"Beda deret (d): {d}")
print(f"Jumlah dari 8 suku pertama: {jumlah_suku_pertama_8}")