while True:
    print("\n=== Program Penghitung Denda DVD ===")

    hari_pinjam = input("Berapa hari DVD dipinjam? (masukkan angka bulat): ")

    # Validasi input agar hanya angka bulat yang diterima
    if hari_pinjam.isdigit():
        hari_pinjam = int(hari_pinjam)

        if hari_pinjam <= 5:
            denda = 0  # Tidak ada denda jika tepat waktu
        else:
            keterlambatan = hari_pinjam - 5
            denda = keterlambatan * 2500  # Denda Rp2500 per hari keterlambatan

            # Tambahan denda jika keterlambatan lebih dari 10 hari
            if keterlambatan > 10:
                tambahan = ((keterlambatan - 10) // 5) * 5500
                denda += tambahan

        print(f"Total denda yang harus dibayar: Rp{denda}")
    else:
        print("Input tidak valid. Harap masukkan angka bulat!")

    # Menanyakan apakah ingin menghitung kembali
    ulang = input("\nApakah Anda ingin menghitung lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program!")
        break
