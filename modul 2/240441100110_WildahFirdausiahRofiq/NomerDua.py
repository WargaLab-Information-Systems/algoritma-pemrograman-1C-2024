#masukkan variabel
skor_jaka = 1100
ipk_jaka = 3.5

skor_ida = 1000
ipk_ida = 3.5

#persyaratan beasiswa
skor = 1100
ipk = 3.0

#menyeleksi
if skor_jaka >= skor and ipk_jaka >= ipk:
    print("jaka lulus seleksi")
else:
    print("jaka tidak lulus seleksi")

if skor_ida >= skor and ipk_ida >= ipk:
    print("ida lulus seleksi")
else:
    print("ida tidak lulus seleksi")