nama = (input("masukkan nama :"))
nim = int(input("masukkan nim :"))
uts = int(input("masukkan nilai UTS:"))
uas = int(input("masukkan nilai UAS:"))
rata_rata = (uts + uas) / 2

print("Nama anda", nama)
print("NIM anda", nim)
print(f"nilai rata-rata {nama}")

if rata_rata <= 100 and rata_rata >=81 :
    print("anda mendapatkan nilai A")
elif rata_rata <=80 and rata_rata >= 71 :
    print("anda mendapatkan nilai B")
elif rata_rata <= 60 and rata_rata >= 41 :
    print("anda mendapatkan nilai C")
else :
    print("anda mendapatkan nilai E")