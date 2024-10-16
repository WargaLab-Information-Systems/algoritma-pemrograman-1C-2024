<<<<<<< HEAD
# Soal1
# Rumus volume balok statis
# panjang=variabel 20=value
panjang = 20 
lebar = 13
tinggi = 7
Volume_balok = panjang*lebar*tinggi
print("Hasil volume balok dari data tersebut adalah ",Volume_balok)

import math

# Meminta input dari pengguna
diameter = float(input("Masukkan diameter tabung (cm): "))
tinggi = float(input("Masukkan tinggi tabung (cm): "))

# Menghitung jari-jari dari diameter
jari_jari = diameter / 2

# Menghitung volume tabung menggunakan rumus
volume = math.pi * jari_jari**2 * tinggi

# Menampilkan hasil
print(f"Volume tabung dengan diameter {diameter} cm dan tinggi {tinggi} cm adalah {volume:.2f} cm³")
print(str("Volume tabung dengan diameter cm dan tinggi cm adalah cm³"))
=======
# ukuran celengan balok
panjang = 20 #cm
lebar = 13 #cm 
tinggi = 7 #cm
volume_balok = panjang*lebar*tinggi 
print(f"volume celengan balok : {volume_balok} cm³.")

#input ukuran celengan volume_tabung
diameter = 14 #cm
luas_selimut = 440 #cm
jari_jari = diameter / 2
phi = 22/7

# cara untuk menghitung volume celengan tabung
tinggi = luas_selimut / (2*phi*jari_jari)
volume_tabung = phi * jari_jari ** 2 * tinggi
print("tinggi tabung adalah:", tinggi)
print(f"volume celengan tabung : {volume_tabung:}cm³.")

>>>>>>> 5b2a2745de3d4ace16d25ace94d62c2cf5f237d9
