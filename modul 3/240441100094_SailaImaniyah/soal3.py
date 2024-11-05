ulang = "ya"  # Variabel untuk menampung pilihan program

while ulang == "ya": # Looping selama user memilih 'y' 
    hari_terlambat = int(input("Masukkan jumlah hari terlambat: "))
    denda = 0
    cek_hari = 6  # Memulai dari hari ke-6 karena 5 hari pertama tidak dikenakan denda

    while cek_hari <= hari_terlambat:
        if cek_hari <= 10:
            denda += 2500  # Denda Rp2500/hari untuk hari ke-6 hingga ke-10
        else:
            denda += 2500  # Denda Rp2500/hari untuk hari setelah ke-10
            if (cek_hari - 10) % 5 == 0:
                denda += 5500  # Denda tambahan Rp5500 setiap kelipatan 5 hari setelah hari ke-10
        
        cek_hari += 1

    print("Total denda keterlambatan adalah:", denda)
    
    # Menanyakan apakah program ingin menghitung lagi
    ulang = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ")

print("Terima kasih telah menggunakan program ini.")