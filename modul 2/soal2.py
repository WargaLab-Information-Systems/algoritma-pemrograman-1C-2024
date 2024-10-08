#cek peryaratan skor dan ipk Ida,Jaka
#didapat data Jaka dan Ida sebagai berikut 

# Data Jaka
skor_jaka = 1100
ipk_jaka = 3.5

# Data Ida
skor_ida = 1000
ipk_ida = 3.5

# Syarat
syarat_skor = 1100
syarat_ipk = 3.5

# Cek kelulusan Jaka
if skor_jaka >= syarat_skor and ipk_jaka >= syarat_ipk:
    print("Jaka lulus untuk persyaratan beasiswa")
else:
    print("Jaka tidak lulus untuk persyaratan beasiswa")

# Cek kelulusan Ida
if skor_ida >= syarat_skor and ipk_ida >= syarat_ipk:
    print("Ida lulus untuk persyaratan beasiswa")
else:
    print("Ida tidak lulus untuk persyaratan beasiswa")