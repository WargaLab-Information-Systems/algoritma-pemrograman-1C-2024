nama = input("masukan nama:")
nim = int(input("masukkan nim:"))
masukan_nilai_uts = int(input("masukkan nilai uts:"))
masukan_nilai_uas = int(input("masukan nilai uas:"))

# Rumus mencari nilai rata-rata
nilai_rata_rata = (masukan_nilai_uts + masukan_nilai_uas)/2

if nilai_rata_rata >= 81 and nilai_rata_rata <= 100:
    print("anda mendapatkan nilai A")
elif nilai_rata_rata >= 71 and nilai_rata_rata <= 80:
    print("anda mendapatkan nilai B")
elif nilai_rata_rata >= 61 and nilai_rata_rata <= 70:
    print("anda mendapat nilai C")
elif nilai_rata_rata >= 41 and nilai_rata_rata <= 60:
    print("anda mendapatkan nilai D")
elif nilai_rata_rata >= 0 and nilai_rata_rata <= 40:
    print("anda mendapatkan nilai E")
else:
    print("tidak sesuai")

print("nama:", nama)
print("nim anda:", nim)
print("nilai rata rata nilai anda:", nilai_rata_rata)
