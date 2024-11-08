GAJI_HARIAN = 100000
MAX_LEMBUR_HARI = 8
MAX_LEMBUR_MINGGU = 40
BONUS_LEMBUR = {4: 100000, 6: 200000, 8: 300000}

# Variabel untuk akumulasi
total_lembur = 0
total_gaji_lembur = 0

# Input lembur harian dan perhitungan
for hari in range(1, 8):
    lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    
    if lembur > MAX_LEMBUR_HARI:
        print("Lembur melebihi batas harian, tidak dihitung.")
        lembur = 0

    if total_lembur + lembur > MAX_LEMBUR_MINGGU:
        print("Batas lembur mingguan tercapai, lembur dihentikan.")
        break

    total_lembur += lembur

    if lembur >= 8:
        bonus = BONUS_LEMBUR[8]
    elif lembur >= 6:
        bonus = BONUS_LEMBUR[6]
    elif lembur >= 4:
        bonus = BONUS_LEMBUR[4]
    else:
        bonus = lembur * 25000  # Rp25.000 per jam untuk 1-3 jam

    total_gaji_lembur += bonus
    print(f"Bonus lembur hari ini: Rp{bonus}")

# Hitung total gaji
gaji_reguler = GAJI_HARIAN * 7
gaji_total = gaji_reguler + total_gaji_lembur

# Tampilkan hasil
print("\n--- Rekap Gaji Mingguan ---")
print(f"Total lembur: {total_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Gaji reguler: Rp{gaji_reguler}")
print(f"Gaji total: Rp{gaji_total}")
