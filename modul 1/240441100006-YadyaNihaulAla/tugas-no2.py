suku_kelima = 11 
jumlah_suku_kedelapan_dan_keduabelas = 52  

# Menghitung beda deret (d) dan suku pertama (a1)
# Dari suku ke-5: a1 + 4d = 11
# Dari jumlah suku ke-8 dan ke-12: 2a1 + 18d = 52

a5 = suku_kelima
# a1 + 4d = 11 => a1 = 11 - 4d
# 2(11 - 4d) + 18d = 52
# 22 - 8d + 18d = 52
# 10d = 30
d = 3
a1 = 11 - 4 * d

# Menghitung jumlah 8 suku pertama
n = 8
S8 = (n / 2) * (2 * a1 + (n - 1) * d)

print(f"Suku pertama (a1): {a1}")
print(f"Beda deret (d): {d}")
print(f"Jumlah 8 suku pertama Darmaji: {S8}")
