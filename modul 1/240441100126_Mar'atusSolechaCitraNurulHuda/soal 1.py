# MENCARI VOLUME BALOK 

panjang = 20
lebar = 13 
tinggi = 7 
volume_balok = panjang * lebar * tinggi

# MENGHITUNG VOLUME BALOK 
print("berikut ini merupakan luas celengan yang dimiliki citra")
print("untuk mencari volume dari balok kita menggunakan rumus berikut :", "\npanjang * lebar * tinggi", "\n20 * 13 * 7 =")
print(volume_balok)

# VOLUME TABUNG 
diameter_tabung = 14
luas_selimut_tabung = 440 
# HITUNG JARI-JARI TABUNG 
print("menghitung jari-jari")
jari_jari = diameter_tabung / 2
print("hasil dari jari-jari tabung adalah :", jari_jari)
# HITUNG TINGGI TABUNG DARI LUAS SELIMUT 
print("menghitung tinggi tabung dari luas selimut ")
tinggi = luas_selimut_tabung / 22/7 * jari_jari** 2
print("hasil untuk tinggi tabung dari luas selimut adalah : ", tinggi)

# HITUNG VOLUME TABUNG 
volume_tabung = 22/7 * jari_jari**2 * tinggi
print(volume_tabung)

# HASIL HITUNGAN AKHIR 
print("jadi volume dari kedua celengan yang dimiliki citra adalah : ")
hasil_kedua_volume_celengan = volume_balok + volume_tabung
print(" volume celengan balok yaitu : ", volume_balok)
print("volume celengan tabung yaitu : ", volume_tabung) 