nama = input("masukkan nama :")
nim = input ("masukkan nim :")
uts = int(input("masukkan nilai uts :"))
uas = int(input("masukkan nilai uas :"))

print("nama:" ,nama)
print("nim:", nim)
nilai_rata_rata =(uts + uas) 
hasil_rata_rata = nilai_rata_rata / 2
print("nilai rata-rata anda adalah", hasil_rata_rata)

if hasil_rata_rata > 100:
    print("data not valid")
elif hasil_rata_rata  > 80 < 100:
    print("anda mendapatkan nilai A")
elif hasil_rata_rata > 70 < 80:
    print("anda mendapatkan nilai B")
elif hasil_rata_rata > 60 < 70:
    print("anda mendapatkan nilai C")
elif hasil_rata_rata > 40 < 60:
    print("anda mendapatkan nilai D")
else:
    print("anda mendapatkan nilai E")
