nama = input("masukkan nama: ")
nim = input("masukka nim: ")
nilai_uts = int(input("masukkan nilai uts: "))
nilai_uas = int(input("masukkan nilai uas: "))

nilai_rata_rata = (nilai_uts + nilai_uas) / 2

if 81 <= nilai_rata_rata <= 100:
    nilai = "A"
elif 71 <= nilai_rata_rata <= 80:
    nilai = "B"
elif 61 <= nilai_rata_rata <= 70:
    nilai = "C"
elif 41 <= nilai_rata_rata <= 60:
    nilai = "D"
elif 0 <= nilai_rata_rata <= 40:
    nilai = "E"
else:
    nilai = "tidak ada nilai"

print("masukkan nama",nama)
print("masukkan nim",nim)
print("nilai rata rata anda",nilai_rata_rata)
print("anda mendapatkan nilai",nilai)