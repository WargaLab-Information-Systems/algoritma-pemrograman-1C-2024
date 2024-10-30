while True:
    lama_penyewaan = int(input("Masukkan lama penyewaan DVD anda (dalam hari): "))

    batas_peminjaman = 5
    denda_per_hari = 2500
    denda_tambahan = 5500

    keterlambatan = lama_penyewaan - batas_peminjaman

    if keterlambatan <= 0:
        total_denda = 0
        print("Anda tidak dikenai denda, terima kasih.")
    else:
        total_denda = keterlambatan * denda_per_hari

        if keterlambatan > 10:
            tambahan_hari = keterlambatan - 10
            denda_ekstra = (tambahan_hari // 5) * denda_tambahan
            total_denda += denda_ekstra

        print(f"Total denda yang harus dibayar: Rp{total_denda}")

    ulangi = input("Apakah anda ingin menghitung kembali? (y/n): ").lower()
    if ulangi != 'y':
        break
