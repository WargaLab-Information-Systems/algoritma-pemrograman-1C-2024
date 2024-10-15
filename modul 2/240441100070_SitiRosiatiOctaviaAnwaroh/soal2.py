# Data mahasiswa
nama_jaka = "Jaka"
skor_jaka = 1100
ipk_jaka = 3.5

nama_ida = "Ida"
skor_ida = 1000
ipk_ida = 3.5

# Syarat beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Mengecek siapa yang lulus persyaratan
if skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_jaka} lulus persyaratan beasiswa.")
else:
    print(f"{nama_jaka} tidak lulus persyaratan beasiswa.")

if skor_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print(f"{nama_ida} lulus persyaratan beasiswa.")
else:
    print(f"{nama_ida} tidak lulus persyaratan beasiswa.")
