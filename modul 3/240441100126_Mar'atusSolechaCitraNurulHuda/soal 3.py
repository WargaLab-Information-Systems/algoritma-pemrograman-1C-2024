while True :
    lama_sewa = int(input("masukkan lama penyewaan DVD : "))
    denda_pokok = 2500
    denda_tambahan = 5500

    if lama_sewa <= 5 :
        print(("anda mengembalikkan tepat waktu"))
    else :
        keterlambatan = lama_sewa - 5 
        denda = keterlambatan * denda_pokok

        if keterlambatan > 10 :
            # lama_keterlambatan = lama_sewa - 5 
            denda_tambahan = (keterlambatan // 5) * denda_tambahan
            denda += denda_tambahan 

        print("total denda keterlambatan yang anda bayar adalah : Rp", denda)

    lanjut = input("Ingin menghitung lagi? (ya/tidak): ").lower()
    if lanjut != 'ya':
        break