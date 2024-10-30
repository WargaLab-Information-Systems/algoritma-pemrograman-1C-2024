while True:
    lama_peminjaman = int(input("Masukkan lama waktu penyewaan (hari): "))

    #Lama Peminjaman
    batas_waktu= 5
    denda_perhari= 2500
    denda_tambahan_per_5_hari= 5500

    #Menghitung Keterlambatan
    if lama_peminjaman <= batas_waktu:
        denda=0
        print("Tidak ada denda karena penyewaan masih dalam batas waktu.")
    else :
        keterlambatan= lama_peminjaman-batas_waktu
        denda= keterlambatan*denda_perhari
    
        #Jika Keterlambatan Lebih Dari 10 hari
        if keterlambatan > 10:
            denda_tambahan_per_5_hari = (keterlambatan - 10)//5
            denda += denda_tambahan_per_5_hari * denda_tambahan_per_5_hari
    
    #Hasil Denda
    print(f"Total denda keterlambatan: Rp{denda}")
    
    lama_peminjaman = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if lama_peminjaman != "ya":
        break
    