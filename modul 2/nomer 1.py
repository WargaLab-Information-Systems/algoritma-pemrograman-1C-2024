nama = (input("Masukkan Nama"))
nim = int(input("Masukkan Nomer NIM"))
nilai_uts = int(input("Masukkan Nilai UTS"))
nilai_uas = int(input("Masukkan Nilai UAS"))

nilai_ratarata = (nilai_uts + nilai_uas) / 2
print("Nilai rata rata anda adalah ", nilai_ratarata)

if nilai_ratarata >= 81 and nilai_ratarata <= 100:
    grade = "A"
elif nilai_ratarata >= 71 and nilai_ratarata <= 80:
    grade = "B"
elif nilai_ratarata >= 61 and nilai_ratarata <= 70:
    grade = "C"
elif nilai_ratarata >= 41 and nilai_ratarata <= 60:
    grade = "D"
elif nilai_ratarata >= 40 and nilai_ratarata <= 0:
    grade = "E"
else:
    grade = "Tidak ada nilai"


print("Nama anda :", nama)
print("NIM anda :", nim)
print("Nilai rata-rata anda :", nilai_ratarata)
print("Anda mendapatkan nilai :", grade)