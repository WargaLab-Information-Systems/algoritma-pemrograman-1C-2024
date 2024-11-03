gaji_harian = 100000
total_gaji_mingguan = 0
total_gaji_lembur = 0
total_lembur_mingguan = 0

for hari in range(7):
    lembur_hari = int(input(f"Masukkan jam lembur untuk hari ke-{hari + 1}: "))
    
    # Setel ulang gaji harian
    gaji_hari = gaji_harian

    # Jika lembur melebihi 8 jam, tidak dihitung
    if lembur_hari > 8:
        print("Lembur melebihi batas, tidak akan dihitung.")
        lembur_hari = 0
    # Jika total lembur lebih dari 40 jam dalam seminggu, batasi hingga 40 jam
    elif total_lembur_mingguan + lembur_hari > 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        lembur_hari = max(0, 40 - total_lembur_mingguan)
        
    # Hitung tambahan gaji lembur berdasarkan jumlah jam lembur
    if lembur_hari == 0:
        tambahan_lembur = 0
    elif lembur_hari <= 3:
        tambahan_lembur = lembur_hari * 25000
    elif lembur_hari == 4 or lembur_hari == 5:
        tambahan_lembur = 1000004
    elif lembur_hari == 6 or lembur_hari == 7:
        tambahan_lembur = 200000
    elif lembur_hari == 8:
        tambahan_lembur = 300000

    # Perbarui total jam lembur mingguan
    total_lembur_mingguan += lembur_hari
    # Tambahkan gaji lembur ke total gaji lembur mingguan
    total_gaji_lembur += tambahan_lembur
    
    # Tambahkan gaji harian ke total gaji mingguan tanpa lembur
    total_gaji_mingguan += gaji_hari

# Hitung total gaji mingguan termasuk lembur
gaji_total = total_gaji_mingguan + total_gaji_lembur

# Tampilkan hasil akhir
print("Total lembur selama satu minggu:", total_lembur_mingguan, "jam")
print("Total gaji lembur: Rp", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur: Rp", total_gaji_mingguan)
print("Total gaji mingguan termasuk lembur: Rp", gaji_total)
