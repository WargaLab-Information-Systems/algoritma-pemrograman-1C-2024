# Inisialisasi variabel
gaji_harian = 100000
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

# Mengambil input jam lembur untuk 7 hari
for hari in range(1, 8):
    lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))
    
    # Cek lembur
    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0
    elif lembur < 0:
        print("Jam lembur tidak bisa negatif.")
        lembur = 0
    
    # Menghitung gaji lembur
    if lembur >= 4:
        if lembur == 4:
            gaji_lembur = 100000
        elif lembur == 6:
            gaji_lembur = 200000
        elif lembur == 8:
            gaji_lembur = 300000
    elif lembur > 0:
        gaji_lembur = lembur * 25000
    else:
        gaji_lembur = 0

    # Tambahkan gaji harian dan gaji lembur
    total_gaji_mingguan += gaji_harian
    total_gaji_lembur += gaji_lembur
    total_lembur_mingguan += lembur

    # Cek total jam lembur dalam seminggu
    if total_lembur_mingguan >= 40:
        print("Total jam lembur dalam satu minggu sudah mencapai batas maksimum. Lembur dihentikan.")
        break

# Menghitung total gaji mingguan
total_gaji_mingguan += total_gaji_lembur

# Menampilkan hasil
print("\n===== Rincian Gaji Mas Ironi =====")
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_harian * 7}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
