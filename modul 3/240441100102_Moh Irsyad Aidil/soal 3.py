
while True:

        hari_terlambat = int(input("masukan hari keterlambatan : "))
        denda = 0
        if hari_terlambat > 5 :
            if hari_terlambat <= 10 :
                denda = (hari_terlambat - 5) * 2500
            else :
                denda = (10 - 5) * 2500

                hari_tambahan = hari_terlambat - 10
                denda += hari_tambahan * 2500

                denda += (hari_tambahan // 5 ) * 5500
    
        print("Masukkan angka yang valid.")
        print ("total denda keterlambatan : ", denda)
        ulang = input("Ingin menghitung kembali? (ya/tidak): ").lower().strip()
        if ulang != 'ya':
            break


