# #Jawaban Tugas Praktikum No 1
#volume balok
panjang= 20 
lebar= 13
tinggi= 7

VolumeBalok= panjang*lebar*tinggi
print(f"volume celengan balok Andi adalah {VolumeBalok}cm")

# #volume tabung
import math
diameter= 14
LuasSelimut= 440
r= diameter/2
tinggi_tabung= LuasSelimut/(2*math.pi*r)

VolumeTabung= (math.pi*r**2*tinggi_tabung)
print(f"volume celengan tabung andi adalah {VolumeTabung}cm")

# #Jawaban Tugas Praktikum No 2
u5= 11
u8_plus_12= 52

# # u5:a + 4b= 11
# # u8 dan u12:(a + 7b)+(a + 11b) = 52
# # a= 11-4b
# # 2a + 18b= 52
# # 2(11-4b)+18b=52
# # 22-8b+18b= 52
# # -8b+18b=52-52
# # 10b= 30
# # b= 30/10

b= 3
a= u5-4*b
a= -1
n= 8

sn= (n/2)*(2*a+(n-1)*b)
print("jadi, jumlah nilai dari 8 suku  pertama adalah:", sn)

# Jawaban Tugas Praktikum No 3
dolar = 35
rupiah = 15102
tukar = dolar * rupiah  
      
print (f"nominal uang yang suraji dapatkan yaitu {tukar} rupiah") 

# #Jawaban Tugas Praktikum No 4
import math
JumlahOrang= 7
BanyaknyaOrangYangTerpilih= 4
hasil = math.comb(JumlahOrang, BanyaknyaOrangYangTerpilih)
print("banyak cara menentukan tim adalah:",  hasil)