# diketahui
p = 20 #cm
l = 13 #cm
t = 7 #cm
diameter = 14 #cm
luas_selimut = 440 #cm2
phi = 3.14

# rumus volume balok
volume_balok = p*l*t
print("volume balok =" +str(volume_balok) +"cm3")

#rumus volume tabung
#hitung jari-jari
jari_jari = diameter/2
#hitung tinggi menggunakan luas selimut
tinggi = luas_selimut / 2*phi*jari_jari
#hitung volume tabung
volume_tabung = phi * jari_jari**2 * tinggi
print ("volume tabung =" +str(volume_tabung) +"cm3")
print ("volume tabung =",volume_tabung ,"cm3")