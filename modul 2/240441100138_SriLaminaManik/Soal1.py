# Soal 1
# Input data dari pengguna
nama = input("Masukan Nama: ")
nim = int(input("Masukan NIM: "))
uts = float(input("Masukan Nilai UTS: "))
uas = float(input("Masukan Nilai UAS: "))

# Hitung nilai rata_rata
rata_rata = (uts + uas)/ 2
print("nilai rata_rata anda", rata_rata)


if rata_rata >= 81 and rata_rata <= 100:
    print("Anda Mendapatkan nilai A ")
elif rata_rata >= 71 and rata_rata <= 80:
    print("Anda Mendapatkan nilai B")
elif rata_rata >= 61 and rata_rata <= 70:
    print("Anda mendapatkan nilai C")
elif rata_rata >= 41 and rata_rata <= 60:
    print("Anda mendapatkan nilai D")
else : 
    print("Anda mendapatkan nilai E")
