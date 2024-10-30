import math

# > balok
panjang = 20
lebar = 13
tinggi = 7

# > tabung
diameter = 14
luas_selimut = 440

# menghitung volume balok
volume_balok = panjang * lebar * tinggi

# jari-jari tabung
jari_tabung = diameter / 2

# tinggi tabung
tinggi_tabung = luas_selimut / (2 * math.pi * jari_tabung)

# volume tabung
volume_tabung = math.pi * jari_tabung**2 * tinggi_tabung

print(f"Volume balok Andy: {volume_balok} cm³")
print(f"Volume tabung Andy: {volume_tabung} cm³")