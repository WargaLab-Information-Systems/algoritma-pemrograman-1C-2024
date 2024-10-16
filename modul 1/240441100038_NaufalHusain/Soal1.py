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