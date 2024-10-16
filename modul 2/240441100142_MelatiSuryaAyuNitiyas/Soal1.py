# Input data
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
nilai_uts = float(input("Masukkan Nilai UTS: "))
nilai_uas = float(input("Masukkan Nilai UAS: "))

# Menghitung rata-rata
rata_rata = (nilai_uts + nilai_uas) / 2

# Menentukan grade
if 81 <= rata_rata <= 100:
    grade = 'A'
elif 71 <= rata_rata <= 80:
    grade = 'B'
elif 61 <= rata_rata <= 70:
    grade = 'C'
elif 41 <= rata_rata <= 60:
    grade = 'D'
elif 0 <= rata_rata <= 40:
    grade = 'E'
else:
    grade = 'Nilai tidak valid'

# Menampilkan hasil
print(f"\nNama: {nama}")
print(f"NIM anda: {nim}")
print(f"Nilai rata-rata anda: {rata_rata:.2f}")
print(f"Anda Mendapatkan Nilai: {grade}")
