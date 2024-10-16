# Memulai loop agar program bisa diulang
while True:
    # Meminta input jumlah hari keterlambatan dari pengguna
    hari_keterlambatan = int(input("Masukkan jumlah hari keterlambatan: "))

    # Inisialisasi variabel
    denda_per_hari = 2500
    denda_tambahan = 5500
    denda_total = 0

    if hari_keterlambatan <= 5:
        denda_total = 0
        print("Tidak ada denda.")
    else:
        # Hitung denda dasar untuk hari ke-6 sampai hari ke-10
        for hari in range(6 ,min(hari_keterlambatan + 1, 11)):
            denda_total += denda_per_hari

        # Jika keterlambatan lebih dari 10 hari, hitung denda tambahan
        if hari_keterlambatan > 10:
            sisa_hari = hari_keterlambatan - 10
            for hari in range(1, sisa_hari + 1):
                denda_total += denda_per_hari
                if hari % 5 == 0:  # Setiap 5 hari keterlambatan, tambahkan denda tambahan
                    denda_total += denda_tambahan


        # Menampilkan total denda
        print("Total denda yang harus dibayar: Rp", denda_total)

        # Menanyakan apakah pengguna ingin menghitung keterlambatan baru
    ulang = input("Apakah Anda ingin menghitung keterlambatan lagi? (ya/tidak): ").lower()
        # Jika jawabannya 'tidak', keluar dari loop
    if ulang != 'ya':
        print("Program selesai.")
        break  # Menghentikan perulangan