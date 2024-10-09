#f untuk format penulisan string dan memmudahkan untuk memanggil variabel agar tidak perlu koma

#volume balok
panjang = 20
lebar = 13
tinggi = 7

volume_balok = panjang * lebar * tinggi
print(f"Volume celengan balok Andi adalah: {volume_balok} cm3 ")


#volume tabung
diameter = 14
r = diameter/ 2
phi = 22/7
luas_selimut = 440

tinggi_tabung = luas_selimut / (2 * phi * r)
print("tinggi tabung kalian:", tinggi_tabung)

volume_tabung = phi * (r ** 2) * tinggi_tabung
print(f"Volume celengan tabung Andi adalah: {volume_tabung} cm3 ")