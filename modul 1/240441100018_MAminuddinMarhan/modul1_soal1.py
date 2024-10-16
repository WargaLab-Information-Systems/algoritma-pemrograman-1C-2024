# mencari volume balok
panjang = 20
lebar = 13
tinggi = 7
volume = panjang * lebar * tinggi
print(f"Jadi volume celengan balok Andi adalah {volume}cm3")

# mencari volume tabung
diameter = 14
luas_selimut = 440
# untuk mencari volume kita harus mencari jari-jari dan tinggi tabung terlebih dahulu
jari_jari = diameter / 2
pi = 22/7
tinggi_tabung = luas_selimut / (2 * pi * jari_jari)
# jika sudah menemukan tinggi tabung dan jari-jari, maka kita bisa melakukan operasi aritmatika untuk mencari volume
volume_tabung = pi * jari_jari**2 * tinggi_tabung
print(f"Dan volume celengan tabung Andi adalah {volume_tabung}cm3")