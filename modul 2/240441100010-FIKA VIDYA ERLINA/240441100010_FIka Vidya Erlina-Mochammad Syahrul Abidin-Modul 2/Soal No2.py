# Data Mahasiswa
Nama_Jaka= "jaka"
Skor_Jaka= 1101
ipk_Jaka= 3.0

Nama_ida= "ida"
Skor_ida= 1000
ipk_ida= 3.5

# Persyaratan Beasiswa
minimal_skor = 1100
minimal_ipk = 3.0

# Cek siapa yang memenuhi persyaratan beasiswa
if Skor_Jaka > minimal_skor and ipk_Jaka >= minimal_ipk:
    print(Nama_Jaka, "Lulus persyaratan Beasiswa")
else:
    print(Nama_Jaka, "Tidak Lulus persyaratan Beasiswa")

if Skor_ida > minimal_skor and ipk_ida > minimal_ipk:
    print(Nama_ida, "Lulus persyaratan Beasiswa")
else:
    print(Nama_ida, "Tidak Lulus persyaratan Beasiswa")
