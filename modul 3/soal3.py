# menghitung total denda keterlambatan penyewaan DVD

while True:
    # input dari pengguna
    lama_sewa = int(input("Masukkan lama penyewaan (dalam hari): "))
    
    # hitung keterlambatan
    keterlambatan = lama_sewa - 5
    
    # hitung denda
    if keterlambatan <= 0:
        total_denda = 0
    else:
        # denda untuk keterlambatan hingga 10 hari
        total_denda = keterlambatan * 2500
        
        # keterlambatan lebih dari 10 hari
        if keterlambatan > 10:
            tambahan_hari = keterlambatan - 10
            total_denda += (tambahan_hari // 5 + 1) * 5500
    
    # total denda
    print("Total denda keterlambatan: Rp.", total_denda)
    
    # menanyakan apakah ingin menghitung kembali
    ulang = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ")
    if ulang != 'ya':
        break
