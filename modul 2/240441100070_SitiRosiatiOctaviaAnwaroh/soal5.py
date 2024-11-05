# Meminta nama pembeli
nama_pembeli = input("Masukkan nama pembeli: ")

# Cek input usia pembeli
usia_pembeli = int(input("Masukkan usia pembeli: "))

# Cek usia pembeli
if usia_pembeli < 18:
    print("Maaf, usia Anda belum mencukupi untuk melakukan transaksi.")
    exit()  # Mengakhiri program jika usia kurang dari 18
else:
    # Meminta input total belanja
    total_belanja = float(input("Masukkan total belanja (dalam Rp): "))

    # Cek apakah total belanja valid
    if total_belanja < 0:
        print("Total belanja tidak valid! Belanjanya tidak boleh kurang dari 0.")
        exit()  # Mengakhiri program jika total belanja tidak valid

    # Inisialisasi diskon
    diskon = 0

    # Mengecek apakah punya kartu member atau tidak
    kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

    # Cek jika memiliki kartu member
    if kartu_member == 'ya':
        diskon += 15  # Diskon 15% untuk member
    elif kartu_member == 'tidak':
        print("Anda tidak mendapatkan diskon kartu member.")
    else:
        print("Input tidak valid! Silakan masukkan 'ya' atau 'tidak'.")
        exit()  # Mengakhiri program jika input tidak valid

    # Cek diskon berdasarkan total belanja
    if total_belanja > 500000:
        diskon += 10  # Diskon tambahan 10% untuk belanja lebih dari Rp500.000

    # Menghitung total diskon dan total harga setelah diskon
    total_diskon = (diskon / 100) * total_belanja
    total_harga_setelah_diskon = total_belanja - total_diskon

    # Menampilkan hasil
    print(f"\nNama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_belanja:.2f}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:.2f}")