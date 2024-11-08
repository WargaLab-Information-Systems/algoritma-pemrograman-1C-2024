harian = 100000
gaji_reguler_seminggu = 0
lembur_seminggu = 0
total_gaji_lembur = 0
jam_lembur_perhari = [0] * 7
for day in range(7):
    jam_lembur = int(input(f"Jam lembur anda hari ke-{day + 1} (dalam jam): "))
    lembur_seminggu += jam_lembur
    if jam_lembur == 0:
        gaji_lembur = 0
    elif 1 <= jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000
    elif 4 <= jam_lembur <6:
        gaji_lembur = 100000
    elif 6 <= jam_lembur <8:
        gaji_lembur = 200000
    elif jam_lembur >= 8:
        gaji_lembur = 300000
        if 8 < jam_lembur:
            print("Lembur melebihi batas, tidak dihitung")
    if lembur_seminggu >= 40:
        print("Jam lembur anda dalam seminggu melebihi batas, lembur akan dihentikan")
        break
    total_gaji_lembur += gaji_lembur
    jam_lembur_perhari[day] = jam_lembur
gaji_reguler_seminggu = harian * 7
total_gaji = gaji_reguler_seminggu + total_gaji_lembur
print("HASIL: ")
print(f"Total lembur selama 1 minggu: {lembur_seminggu} jam")
print(f"Total gaji lembur: Rp.{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: {gaji_reguler_seminggu}")
print(f"Total gaji mingguan termasuk lembur: Rp.{total_gaji}")