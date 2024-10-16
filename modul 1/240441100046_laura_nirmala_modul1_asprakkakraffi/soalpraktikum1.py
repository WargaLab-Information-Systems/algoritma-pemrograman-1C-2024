#volume_balok
panjang = 20
lebar = 15
tinggi = 7

volume_balok = panjang * lebar * tinggi
print(f"volume celengan balok andi: {volume_balok} cm^3")

# volume tabung 
diameter = 14
r = diameter / 2
phi = 22/7
luas_selimut = 440

tinggi_tabung = luas_selimut / (2 * phi * r)
print("tinggi tabung adalah:", tinggi_tabung)

volume_tabung = phi * (r ** 2) * tinggi_tabung
print(f"volume celengan tabung andi adalah: {volume_tabung} cm^3")
