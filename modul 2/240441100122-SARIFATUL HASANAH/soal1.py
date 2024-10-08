nama = input("Masukkan Nama : ")
nim = int(input("Masukkan NIM : "))
uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))
rata_rata = (uts + uas) / 2

print("Nama Anda",nama)
print("NIM Anda :",nim)
print(f"Nilai rata-rata {nama} adalah {int(rata_rata)}")

 
if rata_rata <= 100 and rata_rata >= 81 :
    print("Anda Mendapatkan Nilai A")
elif  rata_rata <= 80 and rata_rata >= 71 :
    print("Anda Mendapatkan Nilai B")
elif  rata_rata <= 70 and rata_rata >= 61 :
    print("Anda Mendapatkan Nilai C")
elif  rata_rata <= 60 and rata_rata >= 41 :
    print("Anda Mendapatkan Nilai D")
elif rata_rata <= 40 and rata_rata >= 0 :
    print("Anda Mendapatkan Nilai E")
else :
    print("Nilai yang dimasukkan salah")


