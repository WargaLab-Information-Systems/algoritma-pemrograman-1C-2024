def input_siswa(klub):
    siswa = set()
    jumlah = int(input(f"Masukkan jumlah siswa yang mengikuti klub {klub}: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama siswa ke-{i+1} yang mengikuti klub {klub}: ")
        siswa.add(nama)
    return siswa

print("Input data siswa untuk klub Basket:")
siswa_basket = input_siswa("Basket")

print("\nInput data siswa untuk klub Renang:")
siswa_renang = input_siswa("Renang")

siswa_kedua_klub = siswa_basket.intersection(siswa_renang)
print("\nDaftar siswa yang mengikuti kedua klub (Basket dan Renang):")
if siswa_kedua_klub:
    for siswa in siswa_kedua_klub:
        print(siswa)
else:
    print("Tidak ada siswa yang mengikuti kedua klub.")

siswa_satu_klub = siswa_basket.symmetric_difference(siswa_renang)
print("\nDaftar siswa yang hanya mengikuti satu klub saja:")
if siswa_satu_klub:
    for siswa in siswa_satu_klub:
        print(siswa)
else:
    print("Tidak ada siswa yang hanya mengikuti satu klub.")

semua_siswa = siswa_basket.union(siswa_renang)
print("\nDaftar semua siswa unik yang mengikuti setidaknya satu klub (Basket atau Renang):")
if semua_siswa:
    for siswa in semua_siswa:
        print(siswa)
else:
    print("Tidak ada siswa yang mengikuti klub.")

print(f"\nJumlah siswa unik yang mengikuti setidaknya satu klub: {len(semua_siswa)}")