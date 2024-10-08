# Input data mahasiswa
nama_jaka = "Jaka"
skor_jaka = 1100
ipk_jaka = 3.5

nama_ida = "Ida"
skor_ida = 1000
ipk_ida = 3.5

# Tentukan syarat beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Cek kelulusan Jaka
if skor_jaka >= skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_jaka} lolos beasiswa.")
else:
    print(f"{nama_jaka} tidak lolos beasiswa.")

# Cek kelulusan Ida
if skor_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print(f"{nama_ida} lolos beasiswa.")
else:
    print(f"{nama_ida} tidak lolos beasiswa.")