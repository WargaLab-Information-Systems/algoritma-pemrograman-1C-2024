# Meminta input dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
uts = int(input("Masukkan Nilai UTS: "))
uas = int(input("Masukkan Nilai UAS: "))

# Menghitung nilai rata-rata
rata_rata = (uts + uas) / 2

# Menyeleksi predikat berdasarkan nilai rata-rata
if rata_rata >= 81:
    predikat = "A"
elif rata_rata >= 71:
    predikat = "B"
elif rata_rata >= 61:
    predikat = "C"
elif rata_rata >= 41:
    predikat = "D"
elif rata_rata >= 30 :
    predikat = "E"
else : 
    predikat = "F"

# Menampilkan hasil
print("Nama:", nama)
print("NIM:", nim)
print("Nilai Rata-Rata:", rata_rata)
print("Mendapatkan Nilai:", predikat)