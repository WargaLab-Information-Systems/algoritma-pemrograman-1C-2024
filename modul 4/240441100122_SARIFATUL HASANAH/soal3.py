gaji_perhari = 100000
total_lembur = 0
total_gaji_lembur = 0
batas_lembur = 40

for hari in range(1, 8):
    jam = int(input(f"Masukkan jam lembur pada hari ke-{hari}: "))

    if jam > 8:
        print("Lembur melebihi batas, hanya dihitung 8 jam.")
        jam = 8
    
    total_lembur += jam

    if 1 <= jam < 4:
        gaji_lembur = jam * 25000
    elif jam == 4:
        gaji_lembur = 100000
    elif jam == 5:
        gaji_lembur = 100000 
    elif jam == 6:
        gaji_lembur = 200000
    elif jam == 7:
        gaji_lembur = 200000
    elif jam == 8:
        gaji_lembur = 300000
    else:
        gaji_lembur = 0

    total_gaji_lembur += gaji_lembur

    print(f"Lembur hari ke-{hari}: {jam} jam, Gaji Lembur: Rp {gaji_lembur}")

    if total_lembur + jam > batas_lembur:
        print("Total lembur melebihi 40 jam dalam seminggu, lembur dihentikan.")
        jam = batas_lembur - total_lembur
        break

total_tanpa_lembur = gaji_perhari * hari
total_plus_lembur = total_tanpa_lembur + total_gaji_lembur

print("\n=== Rincian Gaji Mingguan Mas Ironi ===")
print(f"Total lembur selama seminggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp {total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp {total_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp {total_plus_lembur}")

