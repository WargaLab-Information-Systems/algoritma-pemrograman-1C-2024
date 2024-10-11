nama = input("masukkan nama pembeli: ")
usia = int(input("masukkan usia pembeli: "))

if usia < 18:
    print("maaf usia anda belum mencukupi")
    exit()

#masukkan total belanja
total_belanja = float(input("masukkan total belanja: "))
kartu_member = input("apakah anda memiliki kartu member? (ya/tidak): ")

#diskon
diskon = 0 
if kartu_member == "ya":
    if total_belanja > 500000:
        diskon = 0.25
    else:
        diskon = 0.15
elif total_belanja > 500000:
    diskon = 0.10


#hitung total belanja setelah diskon
diskon_didapat = total_belanja * diskon 
total_setelah_diskon = total_belanja - diskon_didapat

#tampilkan hasil 
print(f"nama pembeli:{nama}")
print(f"{diskon}")
print(f"diskon yang di dapat:Rp{total_belanja}")
print(f"total setelah diskon:Rp{total_setelah_diskon}")