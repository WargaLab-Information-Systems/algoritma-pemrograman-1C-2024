# Input data
nama = input("Masukan Nama: ")
nim = int(input("Masukan NIM: "))
nilai_uts = int(input("Masukan Nilai UTS: "))
nilai_uas = int(input("Masukan Nilai UAS: "))

# Mengitung nilai  rata-rata
nilai_rata_rata = (nilai_uts + nilai_uas) / 2

# Menentukan grade nilai
if nilai_rata_rata >= 81 and nilai_rata_rata <= 100:
  grade = "A"
elif nilai_rata_rata >= 71:
  grade = "B"
elif nilai_rata_rata >= 61:
  grade = "C"
elif nilai_rata_rata >= 41:
  grade = "D"
else:
  grade = "E"

# Menampilkan hasil
print("Masukan Nama:", nama)
print("NIM anda:", nim)
print("Nilai rata rata nilai anda", nilai_rata_rata)
print("Anda Mendapatkan Nilai", grade)