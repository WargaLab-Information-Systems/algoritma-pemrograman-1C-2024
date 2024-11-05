gaji_harian = 100000
total_gaji = 0
total_gaji_lembur = 0
total_jam_lembur_mingguan = 0

for i in range(7):  #iterasi untuk 7 hari dalam seminggu
    jam = int(input(f"Masukkan jam lembur hari ke-{i + 1}: "))
    
    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam = 0

    total_jam_lembur_mingguan += jam
    
    if total_jam_lembur_mingguan >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        jam = 0

    total_gaji += gaji_harian
    
    if jam < 4:
        total_gaji_lembur += jam * 25000
    if jam == 4:
        total_gaji_lembur += 100000
    if jam == 5:
        total_gaji_lembur += 100000
    if jam == 6:
        total_gaji_lembur += 200000
    if jam == 7:
        total_gaji_lembur += 200000
    if jam == 8:
        total_gaji_lembur += 300000

total_gaji += total_gaji_lembur

print("Total jam lembur selama satu minggu:", total_jam_lembur_mingguan)
print("Total gaji lembur:", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur:", gaji_harian * 7)
print("Total gaji mingguan termasuk lembur:", total_gaji)