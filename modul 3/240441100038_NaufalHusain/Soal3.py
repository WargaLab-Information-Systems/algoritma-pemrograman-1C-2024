# membuat loop yang berjalan tanpa henti sebelum kondisi terpenuhi
while True:
    hari_terlambat = input("Masukkan hari terlambat: ")
    
    # Mengecek apakah input adalah angka positif
    if hari_terlambat.isdigit() and int(hari_terlambat) >= 0:
        hari_terlambat = int(hari_terlambat)
        denda = 0

        # Menghitung denda
        if hari_terlambat > 5:
            if hari_terlambat <= 10:
                denda = (hari_terlambat - 5) * 2500
            else:
                denda = 5 * 2500 
                hari_terlambat -= 10
                denda += hari_terlambat * 2500 
                denda += (hari_terlambat // 5) * 5500

        print("Total denda terlambat: ", denda)
    else:
        print("Masukkan angka yang valid")
        continue
    
    # Menanyakan apakah ingin menghitung kembali
    ulang = input("Ingin menghitung kembali? (ya/tidak): ")
    if ulang.lower() != "ya":
        break