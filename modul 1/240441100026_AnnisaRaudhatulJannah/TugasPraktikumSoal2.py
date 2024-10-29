# Diketahui:
suku_ke_5 = 11
jumlah_suku_ke_8_dan_ke_12 = 52

# Beda deret:
beda = (jumlah_suku_ke_8_dan_ke_12 - 2 * suku_ke_5) / 3

# Suku pertama:
suku_pertama = suku_ke_5 - 4 * beda

# Menghitung jumlah 8 suku pertama:
jumlah_8_suku = 8 * suku_pertama + (8 * (8 - 1) / 2) * beda

# Output
print("Jumlah 8 suku pertama deret aritmatika:", jumlah_8_suku)