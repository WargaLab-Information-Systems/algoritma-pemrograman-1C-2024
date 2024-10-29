# Gaji harian
gaji_harian = 100000  
total_gaji_reguler = gaji_harian * 7  
total_lembur = 0  
total_jam_lembur = 0  

# Inisialisasi list untuk jumlah jam lembur setiap hari
jam_lembur_per_hari = [0] * 7  

# Input dari pengguna untuk jumlah jam lembur setiap hari selama satu minggu
for i in range(7):
    jam = int(input(f"Masukkan jumlah jam lembur hari ke-{i + 1}: "))
    jam_lembur_per_hari[i] = jam  # Mengisi list menggunakan indeks

# Proses perhitungan gaji lembur
for jam_lembur in jam_lembur_per_hari:
    # Cek jika lembur melebihi batas
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        continue  
    
    # Cek jika total jam lembur sudah mencapai batas mingguan
    if total_jam_lembur + jam_lembur >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        break
    
    total_jam_lembur += jam_lembur  # Tambah jam lembur ke total
    
    # Hitung bonus lembur berdasarkan jam lembur
    if jam_lembur == 0:
        continue  # Tidak ada lembur, tidak ada tambahan
    elif jam_lembur < 4:
        total_lembur += jam_lembur * 25000  # Rp25.000 per jam untuk 1-3 jam
    elif jam_lembur == 4:
        total_lembur += 100000 
    elif jam_lembur == 5:
        total_lembur += 100000
    elif jam_lembur == 6:
        total_lembur += 200000
    elif jam_lembur == 7:
        total_lembur += 200000
    elif jam_lembur == 8:
        total_lembur += 300000  

# Menghitung total gaji mingguan termasuk lembur
total_gaji_mingguan = total_gaji_reguler + total_lembur

# Menampilkan hasil
print("Lembur per hari:", jam_lembur_per_hari)
print("Total lembur selama satu minggu:", total_jam_lembur)
print("Total gaji lembur:", total_lembur)
print("Total gaji mingguan tanpa lembur:", total_gaji_reguler)
print("Total gaji mingguan termasuk lembur:", total_gaji_mingguan)