while True:
    hari_terlambat = input("Masukkan hari keterlambatan: ")
    
    valid_input = True
    for char in hari_terlambat:
        if char < '0' or char > '9':  
            valid_input = False
            break

    if not valid_input:
        print("Masukkan angka yang valid.")
        continue 

   
    hari_terlambat = int(hari_terlambat)
    denda = 0

    if hari_terlambat > 5:
        if hari_terlambat <= 10:
            denda = (hari_terlambat - 5) * 2500
        else:
            denda = (10 - 5) * 2500
            hari_tambahan = hari_terlambat - 10
            denda += hari_tambahan * 2500
            denda += (hari_tambahan // 5) * 5500
        print("Total denda keterlambatan: ", denda)
    else:
        print("Tidak ada denda untuk keterlambatan 5 hari atau kurang.")

    ulang = input("Ingin menghitung kembali? (ya/tidak): ")
    if ulang != 'ya':
        break
