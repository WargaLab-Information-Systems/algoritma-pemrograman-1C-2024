# Nyatakan panjang, lebar, dan tingginya
p = 20
l = 13
t = 7
print(f"Diketahui celengan balok memiliki panjang {p}cm, lebar {l}cm, dan tinggi {t}cm")

# Masukkan input untuk panjang, lebar, dan tinggi balok
# panjang = int(input("Diketahui Andi memiliki sebuah celengan berbentuk kotak dengan panjang: "))
# lebar = int(input("dan lebarnya: "))
# tinggi = int(input("serta memiliki tinggi celengan balok: "))

# Rumus volume balok
V = p * l * t
print("rumus = p x l x t")
print(f"V : {p} x {l} x {t} = {V}cm³")

# Masukkan library math
# import math

#  Nyatakan diameter dan luas selimutnya
# d = 14
# L = 440
# print(f"Celengan tabung Adi memiliki luas selimut {L} cm, dan diameter {d}cm")

# # Mencari jari jari
# r = d / 2

# # Rumus tinggi dari luas selimut
# t = L / (2 * math.pi * r)
# print("Rumus tinggi tabung jika diketahui luas selimut dan diameter = L / 2 x π x r")
# print(f"t : {L} x 2 x 22/7 x {d}/2 = {t}cm")

# # Rumus volume tabung
# V = math.pi * r ** 2 * t
# print("V = π x r² x t")
# print(f"V : 22/7 x {r}² x {t} = {V} cm³")


#  Nyatakan diameter dan luas selimutnya
# d = 14
# L = 440
# print(f"Celengan tabung Adi memiliki luas selimut {L} cm, dan diameter {d}cm")


# menghitung nilai volume tabung
print("cara menghitung volume tabung jika diketahui diameter dan luas selimut dalah sebagai berikut : ")
print("diameter : 14 cm")
print("luas selimut : 440 cm³")
print("langkah pertama yaitu mencari jari-jari, rumus mencari jari jari = diameter : 2 ")
print("langkah kedua yaitu mencari tinggi, rumus mecari jari jari = luas selimut / (2.π.r)")
print("langkah ketiga yaitu menghitung volume tabung dengan rumus = π . r² . t")
# hitung jari jari
diameter = 14
jarijari = diameter / 2
print(f"hasil jarijari: {jarijari}")
# hitung tinggi
luas_selimut = 440
hasil2 = 2 * 22/7 *jarijari
hasil3 = luas_selimut / hasil2
print(f"hasil tinggi: {hasil3}")
# print(int(hasil))
pangkat = jarijari
pangkat2 = 2
hasil4 = pangkat**pangkat2
# print (hasil14)
volume = 22/7 * hasil4 * hasil3
print(f"hasil dari penjumlahan tabung:{volume} cm³")
