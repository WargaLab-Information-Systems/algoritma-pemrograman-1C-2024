# Input nama, nilai UTS, dan nilai UAS dari pengguna
nama_siswa = input("Masukkan nama siswa: ")
nilai_uts = int(input("Masukkan nilai UTS: "))
nilai_uas = int(input("Masukkan nilai UAS: "))

# Menghitung rata-rata nilai UTS dan UAS
rata_rata_nilai = (nilai_uts + nilai_uas) / 2

# Penyeleksian kondisi berdasarkan rata-rata nilai
if 100 >= rata_rata_nilai >= 81:
    grade = 'A'
elif 80 >= rata_rata_nilai >= 71:
    grade = 'B'
elif 70 >= rata_rata_nilai >= 61:
    grade = 'C'
elif 60 >= rata_rata_nilai >= 41:
    grade = 'D'
elif 40 >= rata_rata_nilai >= 0:
    grade = 'E'
else:
    grade = 'Nilai tidak valid'

# Output hasil nama, rata-rata nilai, dan grade
print(str+  "Siswa {nama_siswa} mendapatkan rata-rata nilai {rata_rata_nilai} dan grade {grade}")
