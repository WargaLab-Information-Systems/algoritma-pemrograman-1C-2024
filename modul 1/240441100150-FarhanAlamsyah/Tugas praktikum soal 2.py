suku_5 = 11 
jumlah_suku_8_dan_12 = 52
# Rumus suku ke n = U1 + (n−1) x d
# masukkan suku ke 5
# u5 = a + 4d = 11
# masukkan jumlah suku ke 8 dan 12
# U8 + U12 = 2a + 18d = 52 

# persamaan U5 pindah ruas
# a = 11 - 4d 

# dimasukkan ke persamaan jumlah u8 dan U12 
# 2 (11 - 4d) + 18d = 52 
# 22 - 8d + 18d = 52 
# 10d = 30 
# d = 3 
 
#  Nyatakan variabelnya
d = 3 
# Masukkan ke persamaan U5
a = 11 - 4 * d 
 
# Rumus jumlah suku pertama Sn = n/2 x (U1 + Un)
jumlah_8_suku_pertama = 8 / 2 * (2 * a + (8 - 1) * d) 
print(f"jumlah 8 suku pertama: {jumlah_8_suku_pertama}") 