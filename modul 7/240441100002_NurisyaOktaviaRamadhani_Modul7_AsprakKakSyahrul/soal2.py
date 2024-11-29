# Fungsi untuk meminta input nama siswa
def input_nama_klub(klub_name):
    siswa_klub = set()
    print(f"Masukkan nama siswa yang mengikuti klub {klub_name} :")
    while True:
        nama = input(f"Masukkan nama siswa untuk klub {klub_name}: ")
        if nama == 'end':
            break
        if nama:
            siswa_klub.add(nama)
    return siswa_klub

# a. Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = input_nama_klub("Basket")
klub_renang = input_nama_klub("Renang")

# Siswa yang mengikuti kedua klub
kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:", kedua_klub)

# Siswa yang hanya mengikuti satu klub
hanya_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("Siswa yang hanya mengikuti satu klub:", hanya_satu_klub)

# Semua siswa unik
semua_siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik:", semua_siswa_unik)

# Jumlah siswa unik
jumlah_siswa = len(semua_siswa_unik)
print("Jumlah siswa unik:", jumlah_siswa)