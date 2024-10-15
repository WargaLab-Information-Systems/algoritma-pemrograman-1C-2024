nama= input("masukkan nama ")
nim= input("masukkan NIM ")
uts=float (input("masukkan nilai UTS:"))
uas=float (input("masukkan nilai UAS:"))

rata_rata= (uas+uts)/2

print("Nama anda",nama)
print("NIM anda",nim)
print("nilai rata rata anda",rata_rata)

if 100>=rata_rata>=81:
    print("Anda mendapatkan nilai A")
elif 80>=rata_rata>=71:
    print("Anda mendapatkan nilai B")
elif 70>=rata_rata>=61:
    print("Anda mendapatkan nilai C")
elif 60>=rata_rata>=41:
    print("Anda mendapatkan nilai D")
elif 40>=rata_rata>=0:
    print("anda mandapatkan nilai E")
else:
    print("nilai tidak sesuai")