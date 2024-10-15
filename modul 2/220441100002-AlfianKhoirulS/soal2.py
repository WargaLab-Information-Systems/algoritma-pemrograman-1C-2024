# Data mahasiswa
mahasiswa_1 = {
    "nama": "Jaka",
    "skor": 1100,
    "ipk": 3.5
}

mahasiswa_2 = {
    "nama": "Ida",
    "skor": 1200,
    "ipk": 3.5
}

# Syarat beasiswa
min_skor = 1100
min_ipk = 3.0

# Fungsi untuk mengecek kelulusan beasiswa
def cek_beasiswa(mahasiswa):
    if mahasiswa['skor'] > min_skor and mahasiswa['ipk'] >= min_ipk:
        return f"{mahasiswa['nama']} memenuhi syarat beasiswa."
    else:
        return f"{mahasiswa['nama']} tidak memenuhi syarat beasiswa."

# Mengecek kelulusan beasiswa untuk Jaka dan Ida
hasil_jaka = cek_beasiswa(mahasiswa_1)
hasil_ida = cek_beasiswa(mahasiswa_2)

# Menampilkan hasil
print(hasil_jaka)
print(hasil_ida)
