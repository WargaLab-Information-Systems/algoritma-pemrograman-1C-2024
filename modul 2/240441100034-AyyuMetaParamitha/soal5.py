nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia: "))
total_belanja = float(input("Masukkan total belanja: "))
kartu_member = input("Apakah memiliki kartu member? (ya/tidak): ")
diskon = 0



if usia < 18:
    print("Maaf, usia Anda belum mencukupi.")
else:
     # menghitung diskon
    if kartu_member == "ya":
        diskon += 0.15  # Diskon 15% jika member
    if total_belanja > 500000:
        diskon += 0.10  # Diskon 10% jika belanja lebih dari Rp500.000


    total_diskon = total_belanja * diskon
    total_bayar = total_belanja - total_diskon

    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp {total_belanja}")
    print(f"Total harga setelah diskon: Rp {total_bayar}")