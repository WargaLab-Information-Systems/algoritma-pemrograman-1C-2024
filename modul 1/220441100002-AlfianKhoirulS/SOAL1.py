import math

# Diketahui
panjang_balok = 20  # cm
lebar_balok = 13    # cm
diameter_tabung = 14  # cm
radius_tabung = diameter_tabung / 2  # jari-jari tabung
luas_selimut_tabung = 440  # cm²
# pi = 3,14

# Menghitung tinggi tabung dari luas selimut
# Luas selimut tabung = 2 * π * r * tinggi
tinggi_tabung = luas_selimut_tabung / (2 * math.pi * radius_tabung)

# Menghitung volume balok
# Volume balok = panjang * lebar * tinggi
# Misal tinggi balok dianggap sama dengan lebar (13 cm) sebagai contoh, karena tinggi balok tidak diberikan
tinggi_balok = 7  # Asumsi tinggi sama dengan lebar
volume_balok = panjang_balok * lebar_balok * tinggi_balok

# Menghitung volume tabung
# Volume tabung = π * r² * tinggi
volume_tabung = math.pi * radius_tabung**2 * tinggi_tabung

# Menampilkan hasil
print(f"Volume balok: {volume_balok:.2f} cm³")
print(f"Volume tabung: {volume_tabung:.2f} cm³")
