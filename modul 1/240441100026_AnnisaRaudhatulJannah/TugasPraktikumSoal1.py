# Celengan berbentuk balok
panjang_balok = 20
lebar_balok = 13
tinggi_balok = 440 / (2 * panjang_balok + 2 * lebar_balok)
volume_balok = panjang_balok * lebar_balok * tinggi_balok

# Celengan berbentuk tabung
diameter_tabung = 14
jari_jari_tabung = diameter_tabung / 2
luas_selimut_tabung = 440
tinggi_tabung = luas_selimut_tabung / (2 * 3.14 * jari_jari_tabung)
volume_tabung = 3.14 * jari_jari_tabung**2 * tinggi_tabung

# Output
print("Volume celengan balok:", volume_balok, "cm³")
print("Volume celengan tabung:", volume_tabung, "cm³")