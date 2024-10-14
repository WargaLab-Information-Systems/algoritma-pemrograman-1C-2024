# Input data pembeli
nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

# Cek usia
if usia < 18:
    print("Maaf usia anda belum mencukupi")
else:
    member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
    total_belanja = int(input("Masukkan total belanja: Rp "))

    # Inisialisasi diskon
    diskon = 0

    # Diskon untuk member
    if member == "ya":
        diskon = 0.15  # 15%

    # Diskon tambahan jika belanja > 500.000
    if total_belanja > 500000:
        diskon = 0.10  # 10%

    # Hitung total diskon dan harga setelah diskon
    total_diskon = total_belanja * diskon
    total_bayar = total_belanja - total_diskon

    # Tampilkan hasil
    print(f"Nama Pembeli: {nama}")
    print(f"Diskon yang didapat: {diskon * 100}%")
    print(f"Total harga sebelum diskon: Rp {total_belanja}")
    print(f"Total harga setelah diskon: Rp {total_bayar}")
 