# Diketahui
a5 = 11  # Suku ke-5
total_a8_a12 = 52  # Jumlah suku ke-8 dan ke-12

# Menghitung beda (d) dan suku pertama (a1)
# Persamaan 1: a_1 + 4d = 11
# Dari Persamaan 1: a_1 = 11 - 4d

# Persamaan 2: 2a_1 + 18d = 52
# Substitusi nilai a_1 ke dalam Persamaan 2
# 2(11 - 4d) + 18d = 52
# 22 - 8d + 18d = 52
# 10d = 30
d = 3  # Beda deret
a_1 = 11 - 4 * d  # Suku pertama

# Menghitung jumlah dari 8 suku pertama
n = 8
S_8 = n / 2 * (2 * a_1 + (n - 1) * d)

# Menampilkan hasil
print("suku pertama:", a_1)
print("beda:", d)
print("Jumlah nilai dari 8 suku pertama dari deret aritmatika adalah:", S_8)