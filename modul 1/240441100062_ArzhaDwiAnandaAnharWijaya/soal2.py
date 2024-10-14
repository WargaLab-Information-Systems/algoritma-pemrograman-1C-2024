# Diberikan
suku_ke_5 = 11
suku_ke_8_Plus_suku_ke_12 = 52

# Permisalan : 
# a = suku pertama 
# d = beda deret

# suku ke-5 : a+4d= 11
# suku ke-8 : a+7d
# suku ke-12 : a+11d

# Persamaan dari informasi diatas
# (a + 7d) + (a + 11d)= 52
# 2a + 18d= 52

# Kita ada dua persamaan:
# 1. a + 4d= 11
# 2. 2a + 18d= 52

# Mengubah ruas persamaan pertama dengan tujuan untuk mendapatkan a
# a = 11 - 4d

# Substitusi a ke dalam persamaan yang kedua
# 2(11 - 4d) + 18d= 52
# 22 - 8d + 18d= 52
# - 8d + 18d = 52-22
# 10d= 30
# d= 3

d = 3
a = 11 - 4 * d  # Menghitung a

# Hitung jumlah 8 suku pertama
jumlah_suku_pertama_8 = (8 / 2) * (2 * a + (8 - 1) * d)

# Menampilkan hasil
print(f"Suku pertama (a): {a}")
print(f"Beda deret (d): {d}")
print(f"Jumlah dari 8 suku pertama: {jumlah_suku_pertama_8}")