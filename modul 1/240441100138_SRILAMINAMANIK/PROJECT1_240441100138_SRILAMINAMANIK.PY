# Data balok
panjang = int(input("Masukkan panjang balok: " ))
lebar = int(input("Masukkan lebar balok: "))
tinggi_balok = int(input("Masukkan tinggi balok: "))

#Data tabung
diameter_tabung = int(input("Masukkan diameter tabung: "))
radius_tabung = diameter_tabung / 2
luas_selimut_tabung = 440  
tinggi_tabung = luas_selimut_tabung / (2 * 3.14 * radius_tabung)

volume_balok = panjang * lebar * tinggi_balok
volume_tabung = 3.14 * radius_tabung**2 * tinggi_tabung

print("Hasil dari volume balok:", volume_balok)
print("Hasil dari volume tabung:",volume_tabung)

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
print("Jumlah nilai dari 8 suku pertama dari deret aritmatika adalah:",S_8)

def hitung_nominal_uang_dalam_rupiah():
    # Nominal uang dalam dolar AS
    nominal_uang_dolar_as = 35
    
    # Nilai tukar dolar AS ke rupiah Indonesia (IDR)
    nilai_tukar_idr_per_usd = 15000
    
    # Hitung nominal uang dalam rupiah
    nominal_uang_dalam_rupiah = nominal_uang_dolar_as * nilai_tukar_idr_per_usd
    
    return nominal_uang_dalam_rupiah

# Cetak hasil
hasil = hitung_nominal_uang_dalam_rupiah()
print(f"Nominal uang dalam rupiah: {hasil} IDR")


n = 7 #semua orang
r = 4 #orang yang dipilih

# Menghitung kombinasi C(n,r)
# C(7,4) = 7! / (7-4)!)
# = 7! / (4! * 3!)
# = (7 * 6 * 5 * 4 * 3 * 2 * 1) / (4 * 3 * 2 * 1) (3 * 2 * 1)

tujuh_faktorial = 7 * 6 * 5 * 4 * 3 * 2 * 1
empat_faktorial = 4 * 3 * 2 * 1
tiga_faktorial = 3 * 2 * 1

banyak_cara = tujuh_faktorial / (empat_faktorial * tiga_faktorial)
print("Jumlah cara membentuk tim",banyak_cara)

