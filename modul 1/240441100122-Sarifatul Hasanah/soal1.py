# Data celengan balok
p = 20  
l = 13    
t_balok = 7 

# Menghitung volume balok
volume_balok = p * l * t_balok
print(f"Volume celengan balok Andi adalah {volume_balok} cm³")

# Data celengan tabung
diameter = 14
phi = 22/7  
r = diameter / 2 #7
luas_selimut = 440 

# Menghitung tinggi tabung dari luas selimut
t_tabung = luas_selimut / (2 * phi * r) 
print("Tinggi Tabungnya adalah ",t_tabung)

# Menghitung volume tabung
volume_tabung = phi * (r ** 2) * t_tabung
print(f"Volume celengan tabung Andi adalah  {int(volume_tabung):} cm³")