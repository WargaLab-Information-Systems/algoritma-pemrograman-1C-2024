# Konstanta
Gaji_Harian = 100000
Maksimal_Jam_Lembur = 8
Maksimal_Jam_Lembur_Mingguan = 40

# Inisialisasi variabel
total_gaji_mingguan = 0
total_jam_lembur = 0
total_gaji_lembur = 0

# Loop untuk 7 hari
for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari} (maksimal {Maksimal_Jam_Lembur} jam): "))

    # Validasi jam lembur
    if jam_lembur > Maksimal_Jam_Lembur:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0  # Tidak dihitung lembur
    elif jam_lembur < 0:
        print("Jam lembur tidak boleh negatif.")
        jam_lembur = 0  # Pastikan tidak negatif

    # Hitung gaji lembur
    if jam_lembur >= 4:
        if jam_lembur == 4:
            gaji_lembur = 100000
        elif jam_lembur == 6:
            gaji_lembur = 200000
        elif jam_lembur == 8:
            gaji_lembur = 300000
        else:
            gaji_lembur = 0  # Jika lebih dari 8, tidak dihitung
    else:
        gaji_lembur = jam_lembur * 25000  # Untuk 1-3 jam lembur

    # Tambah gaji harian dan lembur
    total_gaji_mingguan += Gaji_Harian + gaji_lembur
    total_gaji_lembur += gaji_lembur
    total_jam_lembur += jam_lembur

    # Cek batas jam lembur mingguan
    if total_jam_lembur >= Maksimal_Jam_Lembur_Mingguan:
        print("Total jam lembur dalam seminggu mencapai 40 jam, lembur dihentikan.")
        

# Hasil akhir
print("### Total Gaji Mingguan ###")
print(f"Total jam lembur selama satu minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{Gaji_Harian * 7}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")