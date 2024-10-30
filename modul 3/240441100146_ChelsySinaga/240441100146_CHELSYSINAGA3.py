 #Menggunakan loop untuk menghitung denda
while True:
        
# Meminta pengguna untuk memasukkan lama penyewaan
    hari_penyewaan = int(input("Masukkan jumlah hari peminjaman: "))
    hari_terlambat = int(input("Masukkan jumlah hari keterlambatan: "))
# Denda Per hari Keterlambatan
    denda_per_hari = 2500
            
# Denda Tambahan jika keterlambatan lebih dari 10 hari
    denda_tambahan_per_5_hari = 5500

# Menghitung denda dasar
    denda = hari_terlambat * denda_per_hari

# Jika keterlambatan lebih dari 10 hari, tambahkan denda tambahan
    if hari_terlambat > 10:
        
# Hitung berapa banyak kelipatan 5 hari keterlambatan setelah 10 hari pertama
        sisa_hari = hari_terlambat - 5 
        denda_tambahan = (sisa_hari // 5) * denda_tambahan_per_5_hari
        denda += denda_tambahan 

# Menampilkan hasil perhitungan denda
    print(f"Total denda keterlambatan: Rp {denda}")

# Menanyakan apakah ingin menghitung kembali
    ulang = input("Apakah Anda ingin menghitung kembali? (y/n): ")
    if ulang != 'y':
        print("Terima kasih, sampai jumpa!")
        break