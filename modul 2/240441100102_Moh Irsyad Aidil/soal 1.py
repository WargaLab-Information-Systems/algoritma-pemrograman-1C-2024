nama = (input("masukan nama : "))
nim = int(input("masukan nim : "))
uts = int(input("masukan nilai UTS : "))
uas = int(input("masukan nilai UAS : "))
rata_rata = (uts + uas) / 2

print("nama anda", nama)
print("nim anda", nim)
print(f"nilai rata-rata {nama} adalah {int(rata_rata)}")

if rata_rata <= 100 and rata_rata >=81 :
    print("anda mendapatkan nilai A")
elif rata_rata <= 80 and rata_rata >=71 :
    print("anda mendapatkan nilai B")
elif rata_rata <= 70 and rata_rata >= 61 :
    print (" anda mendapatkan nilai C")
elif rata_rata <= 61 and rata_rata >= 41 :
    print (" anda mendapatkan nilai D")
elif rata_rata <= 40 and rata_rata >= 0:
    print ("anda mendapatkan nilai E")
else :
    print ("nilai salah")