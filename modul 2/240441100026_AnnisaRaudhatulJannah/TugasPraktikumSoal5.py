# Input
nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))
is_member = input("Apakah pembeli memiliki kartu member? (y/n): ").lower() == 'y'
harga_total = int(input("Masukkan total harga sebelum diskon: "))

if usia < 18:
    print("Maaf usia anda belum mencukupi")
else:
    # Menghitung Diskon
    diskon = 0 
    if is_member:
        diskon += 0.15
    if harga_total > 500000:
        diskon += 0.10

    # Menghitung Harga Setelah Diskon
    harga_total_setelah_diskon = harga_total * (1 - diskon)

    # Cetak Hasil
    print("Nama Pembeli:", nama)
    print("Diskon yang didapatkan:", diskon * 100, "%")
    print("Total harga sebelum diskon:", harga_total)
    print("Total harga setelah diskon:", harga_total_setelah_diskon)