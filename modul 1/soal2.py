# RUMUS
# Mencari d/selisih
# 2(11 - 4.d) + 18.d = 52
# 22 - 8.d + 18.d = 52
# 10.d = 30
# d = 3

# Mencari a/suku pertama
# a = suku_ke_5 - 4 * d 
# a = hasil suku yang sudah di ketahui - (suku ke berapa-1)* selisih
# a = 11 - 4 *3
# a = -1 

# Diketahui:
# a = suku pertama = -1
# d = Selisih setiap suku = 3

# Suku ke-5 (a + 4.d) = 11

# Suku ke-8 (a + 7.d) + Suku ke-12 (a + 11.d) = 52

# DIKETAHUI
suku_ke_5 = 11
suku_ke_8_dan_12 = 52
d = 3
a = suku_ke_5 - 4 * d

suku=int(input("Masukkan suku yang ingin anda cari: "))

Mencari_suku =a+(suku-1)*d

print(f"Suku ke {suku} bernilai = {Mencari_suku}"  )

# Jumlah dari 8 suku pertama: S8 = (n/2)(2a + (n-1)d)
n =int(input("Masukkan suku deret aritmatika yang ingin di cari : "))
jumlah_8_suku =int(n / 2) * (2 * a + (n - 1) * d)

print(f"Jumlah {n} suku pertama dari deret aritmatika adalah: {jumlah_8_suku}")
