# p= 20 #cm
# l= 13 #cm
# t= 7 #cm 
#   # menghitung volume balok
# v= p*l*t
# print(v)

diameter= 14 #cm
luas_selimut= 440 #cm
phi= 3.14

# #menghitung volume tabung
jari_jari= diameter/2
tinggi= luas_selimut/ 2* phi* jari_jari
volume= phi*jari_jari**5 *tinggi

print(volume)