#Deklarasi Variabel
gaji_harian = 100000  
gaji_lembur_total = 0 
total_jam_lembur_mingguan = 0  
max_lembur_mingguan = 40

#Proses Perhitungan selama 7 hari
for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))

#Batas Max jam lembur perhari
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 8

#Max jam lembur mingguan 
    if total_jam_lembur_mingguan + jam_lembur > max_lembur_mingguan:
        jam_lembur = max_lembur_mingguan - total_jam_lembur_mingguan
        print(f"Lembur dihentikan, sisa lembur yang diperbolehkan: {jam_lembur} jam.")
    total_jam_lembur_mingguan += jam_lembur

#Hitung gaji lembur perhari
    if jam_lembur == 0:
        gaji_lembur = 0 
    elif 1 <= jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000 
    elif jam_lembur == 4:
        gaji_lembur = 100000 
    elif jam_lembur == 6:
        gaji_lembur = 200000  
    elif jam_lembur == 8:
        gaji_lembur = 300000  
    gaji_lembur_total += gaji_lembur
    print(f"Lembur hari ke-{hari}: {jam_lembur} jam, Gaji lembur: Rp{gaji_lembur:,}")
    if total_jam_lembur_mingguan >= max_lembur_mingguan:
        print("Total lembur mencapai batas mingguan (40 jam), lembur tidak dihitung lagi.")
        break
gaji_mingguan_tanpa_lembur = gaji_harian * 7
gaji_mingguan_dengan_lembur = gaji_mingguan_tanpa_lembur + gaji_lembur_total
print("\nRingkasan:")
print(f"Total lembur selama satu minggu: {total_jam_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{gaji_lembur_total:,}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_mingguan_tanpa_lembur:,}")
print(f"Total gaji mingguan termasuk lembur: Rp{gaji_mingguan_dengan_lembur:,}")