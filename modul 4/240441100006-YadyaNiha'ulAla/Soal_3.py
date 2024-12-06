gaji_harian = 100000
max_lembur_per_hari = 8
max_lembur_minggu = 40
total_jam_lembur = 0
total_gaji_lembur = 0
hari_dalam_seminggu = 7

# List
lembur_per_hari = []

for i in range(hari_dalam_seminggu):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{i + 1}: "))

    if jam_lembur > max_lembur_per_hari:
        print("Lembur telah melebihi batas, hanya 8 jam yang dihitung.")
        jam_lembur = max_lembur_per_hari

    lembur_per_hari.append(jam_lembur)

# Max 40 jam
for lembur in lembur_per_hari:
    if total_jam_lembur + lembur <= max_lembur_minggu:
        total_jam_lembur += lembur
        if lembur >= 8:
            total_gaji_lembur += 300000
        elif lembur >= 6:
            total_gaji_lembur += 200000
        elif lembur >= 4:
            total_gaji_lembur += 100000
        else:
            total_gaji_lembur += 25000 * lembur
    else:
        sisa_lembur = max_lembur_minggu - total_jam_lembur
        total_jam_lembur += sisa_lembur

        if sisa_lembur >= 8:
            total_gaji_lembur += 300000
        elif sisa_lembur >= 6:
            total_gaji_lembur += 200000
        elif sisa_lembur >= 4:
            total_gaji_lembur += 100000
        else:
            total_gaji_lembur += 25000 * sisa_lembur
        print("Total lembur telah mencapai batas 40 jam, lembur berikutnya tidak dihitung.")
        break

# total gaji
total_gaji_tanpa_lembur = gaji_harian * hari_dalam_seminggu

# total gaji + lembur
total_gaji_dengan_lembur = total_gaji_tanpa_lembur + total_gaji_lembur

print("--- Ringkasan Gaji Mas Ironi ---")
print(f"Total lembur selama 1 minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur:,}") #:, = pemisah ribuan
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_tanpa_lembur:,}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_dengan_lembur:,}")
