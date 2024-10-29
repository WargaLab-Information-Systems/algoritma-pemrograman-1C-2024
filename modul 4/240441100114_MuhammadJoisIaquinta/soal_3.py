gaji_harian = 100000
total_lembur = 0
total_gaji_lembur = 0
batas_lembur = 40

for hari in range (1, 8):
    if total_lembur > batas_lembur:
           print("total lembur melebihi 40 jam dalam seminggu, lembur diberhentikan")
           break
    else:
        jam = int(input(f"masukkan jam lembur pada hari ke-{hari}: "))
        if jam > 8:
                print("lembur melebihi batas, tidak di hitung")
        total_lembur += jam

        if jam < 4:
                gaji_lembur = jam  * 25000
        elif jam  == 4 or jam == 5:
                gaji_lembur = 100000
        elif jam == 6 or jam == 7:
                gaji_lembur = 200000
        elif jam  == 8:
                gaji_lembur = 300000
        else:
                gaji_lembur = 300000

    total_gaji_lembur += gaji_lembur
    print(f"lembur hari ke-{hari}: {jam} jam, gaji lembur: Rp{gaji_lembur} ")


total_tanpa_lembur = gaji_harian * hari   
total_semua_gaji = total_tanpa_lembur + total_gaji_lembur

print("rincian gaji mingguan")
print(f"total lembur selama seminggu: {total_lembur} jam")
print(f"total gaji lembur: Rp{total_gaji_lembur}")
print(f"total gaji mingguan tanpa lembur: Rp {total_tanpa_lembur}")
print(f"total gaji mingguan termasuk lembur: Rp {total_semua_gaji}")