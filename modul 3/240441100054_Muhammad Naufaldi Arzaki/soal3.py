while True:
    lama_sewa = int(input("Masukkan lama sewa DVD (dalam hari):"))
    
    keterlambatan = lama_sewa - 5

    total_denda = 0
    if keterlambatan > 0:
        total_denda += keterlambatan * 2500

    if keterlambatan > 10:
        denda_tambahan = (keterlambatan - 10) // 5 * 5500

        total_denda += denda_tambahan

    print("Total denda keterlambatan adalah: Rp", total_denda)

    ulang = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        break
        
print("Terima kasih telah menyewa DVD di toko kami!")