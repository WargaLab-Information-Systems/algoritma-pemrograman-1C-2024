while True:
        # Minta input lama penyewaan dari user
        lama_sewa = int(input("Masukkan lama penyewaan DVD (dalam hari): "))
        
        if lama_sewa <= 5:
            print("DVD dikembalikan tepat waktu, tidak ada denda.")
        else:
            # Hitung keterlambatan
            keterlambatan = lama_sewa - 5
            denda = keterlambatan * 2500  # Denda per hari

            # Cek apakah keterlambatan lebih dari 10 hari
            if keterlambatan > 10:
                # Hitung berapa periode 5 hari lebih dari 10
                berat_keterlambatan = keterlambatan - 5
                denda_tambahan = (berat_keterlambatan // 5) * 5500
                denda += denda_tambahan  # Tambahkan denda tambahan

            print(f"Total denda keterlambatan: Rp{denda}")

        # Tanya user apakah mau menghitung lagi
        hitung_lagi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").strip().lower()
        if hitung_lagi != 'ya':
            print("Terima kasih telah menggunakan program ini!")
            break