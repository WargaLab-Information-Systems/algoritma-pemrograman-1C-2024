gaji_harian = 100000  
total_gaji_reguler = gaji_harian * 7  
total_jam_lembur_mingguan = 0  
total_bonus_lembur_mingguan = 0  
lembur_dihentikan = False  # Dihentikan karena mencapai 40 jam

# jam lembur harian
jam_kerja_harian = []
for i in range(7):
    jam = int(input(f"Masukkan jam lembur untuk hari ke-{i + 1} (0-8 jam): "))
    jam_kerja_harian.append(jam)

# Gaji lembur dan total gaji
for hari in range(7):
    jam_lembur = jam_kerja_harian[hari]
    
    if lembur_dihentikan:
        print(f"Hari ke-{hari + 1}: Lembur dihentikan.")
        continue

    # Batas lembur per hari
    if jam_lembur > 8:
        print(f"Hari ke-{hari + 1}: Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0

    # Menambah jam lembur ke total mingguan
    total_jam_lembur_mingguan += jam_lembur
    
    # jika total lembur sudah mencapai atau melebihi 40 jam
    if total_jam_lembur_mingguan >= 40:
        lembur_dihentikan = True
        total_jam_lembur_mingguan = 40  
        print(f"Hari ke-{hari + 1}: Lembur dihentikan karena mencapai batas 40 jam.")

    # Menghitung bonus lembur per hari
    if jam_lembur == 0:
        bonus_lembur_harian = 0
    elif 1 <= jam_lembur <= 3:
        bonus_lembur_harian = 25000 * jam_lembur
    elif jam_lembur == 4:
        bonus_lembur_harian = 100000
    elif jam_lembur == 5:
        bonus_lembur_harian = 150000
    elif jam_lembur == 6:
        bonus_lembur_harian = 200000
    elif jam_lembur == 7:
        bonus_lembur_harian = 250000
    elif jam_lembur == 8:
        bonus_lembur_harian = 300000
    else:
        bonus_lembur_harian = 0

    total_bonus_lembur_mingguan += bonus_lembur_harian
    print(f"Hari ke-{hari + 1}: Lembur {jam_lembur} jam, Bonus lembur: Rp{bonus_lembur_harian}")

# Total gaji mingguan termasuk lembur
total_gaji_mingguan = total_gaji_reguler + total_bonus_lembur_mingguan

print(f"\nTotal lembur selama 1 minggu: {total_jam_lembur_mingguan} jam")
print(f"Total gaji lembur selama 1 minggu: Rp{total_bonus_lembur_mingguan}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
