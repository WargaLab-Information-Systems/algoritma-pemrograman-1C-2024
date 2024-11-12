# Meminta input dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
uts = int(input("Masukkan Nilai UTS: "))
uas = int(input("Masukkan Nilai UAS: "))

# Menghitung nilai rata-rata
rata_rata = (uts + uas) / 2

# Menyeleksi predikat berdasarkan nilai rata-rata
if rata_rata > 100:
    predikat = "data not valid" 
elif rata_rata > 80 < 101:
    predikat = "A"
elif rata_rata > 70 < 80:
    predikat = "B"
elif rata_rata > 60 < 70:
    predikat = "C"
elif rata_rata > 40 < 60:
    predikat = "D"
else:
    predikat = "E"

# Menampilkan hasil
print("Nama Anda:", nama)
print("NIM Anda:", nim)
print("Nilai Rata-Rata Anda:", rata_rata)
print("Anda Mendapatkan Nilai:", predikat)
