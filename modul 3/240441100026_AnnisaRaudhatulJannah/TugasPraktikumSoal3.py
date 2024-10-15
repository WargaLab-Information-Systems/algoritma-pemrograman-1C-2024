denda_harian = 2500
denda_tambahan = 5500
batas_sewa = 5

lama_sewa = int(input("Masukkan lama penyewaan DVD (dalam hari): "))

# Menghitung denda
if lama_sewa <= batas_sewa:
    total_denda = 0
else:
    keterlambatan = lama_sewa - batas_sewa
    total_denda = keterlambatan * denda_harian
    
    # Denda tambahan jika keterlambatan lebih dari 10 hari
    if keterlambatan > 10:
        denda_ekstra = (keterlambatan - 10) // 5 * denda_tambahan
        total_denda += denda_ekstra

print(f"Total denda keterlambatan: Rp {total_denda}")


hitung_lagi = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ").lower()
if hitung_lagi == 'ya':
  
    lama_sewa = int(input("Masukkan lama penyewaan DVD (dalam hari): "))
    
    
    if lama_sewa <= batas_sewa:
        total_denda = 0
    else:
        keterlambatan = lama_sewa - batas_sewa
        total_denda = keterlambatan * denda_harian
        
        if keterlambatan > 10:
            denda_ekstra = (keterlambatan - 10) // 5 * denda_tambahan
            total_denda += denda_ekstra

    
    print(f"Total denda keterlambatan: Rp {total_denda}")
else:
    print("Terima kasih! Program selesai.")
