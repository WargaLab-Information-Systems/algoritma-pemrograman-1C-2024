#skor dan ipk jaka
nama_jaka = "jaka"
score_jaka = 1100
ipk_jaka = 3.5

#skor dan ipk ida
nama_ida = "ida"
score_ida = 1000
ipk_ida = 3.5

# Persyaratan beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Memeriksa kelayakan Jaka
if score_jaka >= skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_jaka} memenuhi persyaratan beasiswa.")
else:
    print(f"{nama_jaka} tidak memenuhi persyaratan beasiswa.")

# Memeriksa kelayakan Ida
if score_ida >= skor_minimal and ipk_ida >= ipk_minimal:
    print(f"{nama_ida} memenuhi persyaratan beasiswa.")
else:
    print(f"{nama_ida} tidak memenuhi persyaratan beasiswa.")
