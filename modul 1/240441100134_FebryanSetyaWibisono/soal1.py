panjang = 20
lebar = 13
tinggi = 7
diameter = 14
luas_selimut = 440
jari_jari = diameter / 2
pi = 22/7

# luas selimut = 2*pi*r*t
# 440 = 2*22/7*7*7
# 440 = 44*7

tinggi_tabung = 440 / 44 # hasilnya 10
volume_balok = panjang * lebar * tinggi
volume_tabung = pi * jari_jari**2 * tinggi_tabung 
print("Jadi hasil dari volume balok adalah", volume_balok)
print(f"Jadi hasil dari volume tabung adalah {volume_tabung}")