nama = input("Masukkan nama anda: ")
nim = int(input("Masukkan NIM anda: "))
n_uts = int(input("Masukkan nilai UTS anda: "))
n_uas = int(input("Masukkan nilai UAS anda: "))

hitung_rata_rata = (n_uts + n_uas) / 2

if hitung_rata_rata > 100:
    deskripsi = "Nilai tidak Sesuai"
elif hitung_rata_rata >= 81 and hitung_rata_rata <= 100:
    deskripsi = "A"
elif hitung_rata_rata >= 71 and hitung_rata_rata <= 80:
    deskripsi = "B"
elif hitung_rata_rata >= 61 and hitung_rata_rata <= 70:
    deskripsi = "C"
elif hitung_rata_rata >= 41 and hitung_rata_rata <= 60:
    deskripsi = "D"
else:
    deskripsi = "E"

print(f"Nama anda: {nama}")
print(f"NIM anda: {nim}")
print(f"Nilai rata-rata anda: {hitung_rata_rata}")
print(f"Anda mendapatkan nilai: {deskripsi}")
