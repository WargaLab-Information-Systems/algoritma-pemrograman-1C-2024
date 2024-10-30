nama= input ("Masukan Nama = ")
nim=int(input("Masukan Nim = "))
Uts= float(input("Masukan nilai UTS: "))
uas= float(input("Masukan nilai UAS: "))
rata= (Uts+uas)/2
print("Masukan  Nama",nama)
print("Masukan  Nim",nim)
print("nilai rata-rata nilai anda",rata)
if rata>=81 and rata<=100:
    print("anda mendapatkann nilai A")
if rata>=71 and rata<=80:
    print("anda mendapatkann nilai B")
if rata>=61 and rata<=70:
    print("anda mendapatkann nilai C")
if rata>=41 and rata<=60:
    print("anda mendapatkann nilai D")
if rata>=0 and rata<=40:
    print("anda mendapatkann nilai E")
    
