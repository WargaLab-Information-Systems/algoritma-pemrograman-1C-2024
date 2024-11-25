nama_pembeli = input("masukkan nama anda: ")
usia = int(input("berapa usia anda: "))
nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))
total_harga = float(input("Masukkan total harga belanja: "))
kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak):").strip().lower()

if usia < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    diskon = 0

    
    if kartu_member == "ya":
        diskon = 15
    if total_harga > 500000:
        diskon = max(diskon, 10)

    total_diskon = (diskon / 100) * total_harga
    total_harga_setelah_diskon = total_harga - total_diskon

    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapat: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_harga:.2f}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:.2f}")