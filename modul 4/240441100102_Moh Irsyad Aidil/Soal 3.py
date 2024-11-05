gaji_harian = 100000
total_gaji_mingguan = 0
total_gaji_lembur = 0
total_lembur_mingguan = 0

for hari in range(7):
    lembur_hari = int(input(f"Masukkan jam lembur untuk hari ke-{hari + 1 }: "))

    gaji_hari = gaji_harian
    
    if lembur_hari >= 8:
        print("Lembur melebihi batas, tidak akan dihitung.")
        lembur_hari = 0
    elif total_lembur_mingguan + lembur_hari >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        lembur_hari = 0
    else:
        # Hitung gaji lembur dalam satuan jam nya mas ironi
        if lembur_hari == 0:
            tambahan_lembur = 0
        elif lembur_hari <=3 :
            tambahan_lembur = lembur_hari * 25000
        elif lembur_hari == 4:
            tambahan_lembur = 100000
        elif lembur_hari == 5:
            tambahan_lembur == 100000
        elif lembur_hari == 6:
            tambahan_lembur = 200000
        elif lembur_hari == 7:
            tambahan_lembur == 200000
        elif lembur_hari == 8:
            tambahan_lembur = 300000
        
        # Update total lembur dan gaji lembur
        total_lembur_mingguan += lembur_hari
        total_gaji_lembur += tambahan_lembur
        gaji_hari += gaji_harian * 7
    
    # Tambahkan gaji harian ke total gaji mingguan
    total_semua_gaji = total_gaji_lembur + gaji_harian * 7
    
    # Cetak hasil harian
    print(f"lembur hari ke-{hari}: {lembur_hari} jam, gaji lembur: Rp{tambahan_lembur} ")


print("\nTotal lembur selama satu minggu:", total_lembur_mingguan, "jam")
print("Total gaji lembur: Rp", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur: Rp", gaji_harian * 7)
print("Total gaji mingguan termasuk lembur: Rp", total_semua_gaji)