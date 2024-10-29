# Nyatakan panjang, lebar, dan tingginya
panjang = 20
lebar = 13
tinggi = 7
print(f"Diketahui celengan balok memiliki panjang {panjang}cm, memiliki lebar {lebar}cm, dan tinggi {tinggi}cm")

# Masukkan input untuk panjang, lebar, dan tinggi balok
# panjang = int(input("Diketahui Andi memiliki sebuah celengan berbentuk kotak dengan panjang: "))
# lebar = int(input("dan lebarnya: "))
# tinggi = int(input("serta memiliki tinggi celengan balok: "))

# Rumus volume balok
volume_balok = panjang * lebar * tinggi
print("rumus balok = p x l x t")
print(f"Volume balok: {panjang} x {lebar} x {tinggi} = {volume_balok}cm³")

# Masukkan library math
import math

# Nyatakan diameter dan luas selimutnya
diameter = 14
luas_selimut = 440
print(f"Celengan tabung Adi memiliki luas selimut {luas_selimut} cm, dan diameter {diameter}cm")

# Mencari jari jari
r = diameter / 2

# Rumus tinggi dari luas selimut
tinggi_tabung = luas_selimut / (2 * math.pi * r)
print("Rumus tinggi tabung jika diketahui luas selimut dan diameter = luas selimut / 2 x π x r")
print(f"Tinggi tabung: {luas_selimut} x 2 x 22/7 x {diameter}/2 = {tinggi_tabung}cm")
print("volume",volume_balok)
# Rumus volume tabung
volume_tabung = math.pi * r ** 2 * tinggi_tabung
print("volume tabung = π x r² x t")
print(f"Volume tabung: 22/7 x {r}² x {tinggi_tabung} = {volume_tabung} cm³")
