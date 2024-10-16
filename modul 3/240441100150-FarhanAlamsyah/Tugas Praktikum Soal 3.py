denda = 2500
denda_tambahan = 5500

while True:
    lama_sewa = input("Lama hari sewa DVD: ")
    if lama_sewa.isdigit():
        keterlambatan = int(lama_sewa) - 5

        total_denda = 0
        if keterlambatan > 5:
            total_denda = keterlambatan * denda
            if keterlambatan > 10:
                total_denda += ((keterlambatan - 5) // 5) * denda_tambahan 
        print(f"Total denda keterlambatan: Rp {total_denda}")
    else:
        print("Input tidak valid! Harap masukkan angka yang benar.")

    hitung_lagi = input("Apakah Anda ingin menghitung kembali? (iya/tidak): ")
    if hitung_lagi != 'iya':
        print("Terima kasih telah menggunakan program ini.")
        break