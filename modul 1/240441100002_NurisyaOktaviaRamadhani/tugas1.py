#balok
panjang = float(input("Masukkan panjang balok: " ))
lebar = float(input("Masukkan lebar balok: "))
tinggi_balok = float(input("Masukkan tinggi balok: "))

#tabung
diameter_tabung = float(input("Masukkan diameter tabung: "))
radius_tabung = diameter_tabung / 2
luas_selimut_tabung = 440  
tinggi_tabung = luas_selimut_tabung / (2 * 3.14 * radius_tabung)

volume_balok = panjang * lebar * tinggi_balok
volume_tabung = 3.14 * radius_tabung**2 * tinggi_tabung

print("Hasil dari volume balok:", volume_balok)
print("Hasil dari volume tabung:", volume_tabung)