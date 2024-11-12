nama_pembeli = input("Masukkan Nama Pembeli: ")
usia = int(input("Masukkan Usia Pembeli: "))

# Cek usia
if usia < 18:
    print("Maaf, usia anda belum mencukupi")
else:
    total_belanja = float(input("Masukkan Total Belanja: Rp "))
    kartu_member = input("Apakah memiliki kartu member? (y/n): ")

    diskon = 0
    if kartu_member.lower() == 'y':
        diskon += 0.15  # Diskon 15% untuk member
    if total_belanja > 500000:
        diskon += 0.10  # Diskon 10% jika belanja lebih dari Rp500.000

    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang Didapatkan: {diskon*100}%")
    print(f"Total Belanja Sebelum Diskon: Rp {total_belanja}")
    print(f"Total Belanja Setelah Diskon: Rp {total_setelah_diskon}")
