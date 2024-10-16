
# Menghitung volume celengan balok
panjang = 20  # cm
lebar = 13    # cm
tinggi = 7    # cm
volume_balok = panjang * lebar * tinggi
pi = 22/7
# Menghitung volume celengan tabung
diameter = 14  # cm
jari_jari = diameter / 2
luas_selimut = 440  # cm²

# Menghitung tinggi tabung dari luas selimut
tinggi_tabung = luas_selimut / (2 * pi * jari_jari)

# Menghitung volume tabung
volume_tabung = pi * jari_jari**2 * tinggi_tabung

# Menampilkan hasil
print(f"Volume celengan balok: {volume_balok} cm³")
print(f"Volume celengan tabung: {volume_tabung:.2f} cm³")

