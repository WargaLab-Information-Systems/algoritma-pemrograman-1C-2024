def input_siswa_klub(klub):
    print(f"Masukkan nama siswa yang mengikuti klub {klub} :")
    input_data = input()
    siswa_set = set(input_data.split(','))
    return siswa_set

set_basket = input_siswa_klub("Basket")
set_renang = input_siswa_klub("Renang")

# daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = set_basket & set_renang  # Intersection
print("\nSiswa yang mengikuti kedua klub:", siswa_kedua_klub)

# daftar siswa yang hanya mengikuti satu klub
siswa_satu_klub = set_basket ^ set_renang  # Symmetric difference
print("\nSiswa yang hanya mengikuti satu klub:", siswa_satu_klub)

#  daftar semua siswa unik yang mengikuti setidaknya satu klub
siswa_unik = set_basket | set_renang  # Union
print("\nSiswa yang mengikuti setidaknya satu klub:", siswa_unik)

# jumlah siswa unik yang mengikuti setidaknya satu klub
jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)

