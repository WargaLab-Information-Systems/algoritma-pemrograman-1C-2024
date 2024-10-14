# Program untuk menghitung denda keterlambatan penyewaan DVD

while True:
    # Loop untuk meminta input dari pengguna
    for _ in range(1):  # Menggunakan range(1) untuk loop satu kali
        lama_sewa = input("Masukkan lama untuk sewa DVD (dalam satuan hari): ")

        if lama_sewa.isdigit():  # Memeriksa apakah input adalah angka positif
            lama_sewa = int(lama_sewa)

            if lama_sewa < 0:
                print("Lama sewa tidak bisa negatif. Silakan coba lagi.")
                continue

            denda_harian = 2500
            denda_tambahan = 5500
            batas_tambahan = 10
            
            if lama_sewa <= 5:
                total_denda = 0  # Tidak ada denda jika dikembalikan tepat waktu
            else:
                keterlambatan = lama_sewa - 5
                total_denda = keterlambatan * denda_harian
                
                if keterlambatan > batas_tambahan:
                    tambahan_hari = keterlambatan - batas_tambahan
                    total_denda += (tambahan_hari // 5 + 1) * denda_tambahan
            
            print(f"Total denda keterlambatan: Rp{total_denda}")

        else:
            print("Input tidak valid. Silakan masukkan angka dalam satuan hari yang benar.")

    ulang = input("Apakah anda Ingin menghitung kembali? (ya/tidak): ")
    if ulang != "ya":
        break
