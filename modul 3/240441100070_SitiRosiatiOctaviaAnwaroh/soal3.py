while True:
    # Meminta input dari pengguna
    lama_peminjaman = input("Masukkan lama peminjaman DVD (dalam hari): ")
    
    # Memastikan input adalah angka
    if not lama_peminjaman.isdigit():  # Memeriksa apakah input adalah angka
        print("Input tidak valid! Silakan masukkan angka yang valid.")
        continue

    # Konversi input ke integer
    lama_peminjaman = int(lama_peminjaman)

    # Validasi untuk angka negatif
    if lama_peminjaman < 0:
        print("Lama peminjaman tidak boleh negatif!")
        continue

    # Mengatur nilai denda dan batas peminjaman
    denda_harian = 2500  # Denda per hari
    denda_tambahan = 5500  # Denda tambahan per 5 hari setelah 10 hari keterlambatan
    batas_peminjaman = 5  # Batas waktu peminjaman

    # Menghitung keterlambatan
    if lama_peminjaman <= batas_peminjaman:
        total_denda = 0  # Tidak ada denda
    else:
        keterlambatan = lama_peminjaman - batas_peminjaman
        total_denda = keterlambatan * denda_harian

        # Tambahan denda jika keterlambatan lebih dari 10 hari
        if keterlambatan > 10:
            denda_tambahan_hari = (keterlambatan - 10) // 5
            total_denda += denda_tambahan_hari * denda_tambahan

    # Menampilkan hasil
    if total_denda > 0:
        print(f"Total denda keterlambatan untuk {lama_peminjaman} hari: Rp{total_denda}")
    else:
        print("Tidak ada denda keterlambatan.")

    # Menanyakan kepada pengguna apakah ingin menghitung lagi
    lagi = input("Apakah Anda ingin menghitung denda lagi? (ya/tidak): ")
    if lagi != 'ya':  # Menggunakan lower() untuk memastikan perbandingan tidak case-sensitive
        print("Terima kasih telah menggunakan program ini!")
        break
