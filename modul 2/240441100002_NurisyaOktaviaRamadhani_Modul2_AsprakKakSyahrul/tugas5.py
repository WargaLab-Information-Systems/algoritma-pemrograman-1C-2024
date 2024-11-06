nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))
if usia < 18:
    print("Maaf usia anda belum mencukupi.")
else:
    total_belanja = float(input("Masukkan total belanja: Rp"))
    member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
    diskon = 0 
    if member == "ya":
        diskon += 15  
    if total_belanja > 500000:
        diskon += 10  
    total_diskon = total_belanja * (diskon / 100)
    total_setelah_diskon = total_belanja - total_diskon
    print("\n--- Rincian Pembelian ---")
    print(f"Nama Pembeli        : {nama}")
    print(f"Total Harga Sebelum Diskon : Rp{total_belanja}")
    print(f"Diskon yang Didapat : {diskon}%")
    print(f"Total Diskon        : Rp{total_diskon}")
    print(f"Total Harga Setelah Diskon : Rp{total_setelah_diskon}")