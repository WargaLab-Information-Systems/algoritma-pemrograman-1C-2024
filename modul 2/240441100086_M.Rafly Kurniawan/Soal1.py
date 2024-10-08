nama = input("masukkan Nama anda : ")
nim = int(input("masukkan NIM : "))
nilai_uts = int(input("masukkan nilai UTS : "))
nilai_uas = int(input("masukkan nilai UAS : "))
nilai_rata_rata = (nilai_uts + nilai_uas) / 2

print("Nama anda", nama)
print("NIM anda", nim)
print(f"nilai rata-rata {nama} adalah {int(nilai_rata_rata)}")


if nilai_rata_rata <= 100 and nilai_rata_rata >=81 :
    print("anda mendapatkan nilai A")
elif nilai_rata_rata <= 80 and nilai_rata_rata >= 71 :
    print("anda mendapatkan nilai B")
elif nilai_rata_rata <= 70 and nilai_rata_rata >= 61 :
    print("anda mendapatkan nilai C")
elif nilai_rata_rata <= 60 and nilai_rata_rata >= 41 :
    print("anda mendapatkan nilai D")
elif nilai_rata_rata <= 40 and nilai_rata_rata >= 0 :
    print("anda mendapatkan nilai E") 
else :
    print("nilai yang dimasukkan salah")