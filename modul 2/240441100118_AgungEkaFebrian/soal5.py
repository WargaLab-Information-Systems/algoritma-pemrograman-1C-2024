nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

if usia < 18:
    print("Maaf anda belum cukup usia untuk melakukan transaksi.")
else:
    total_belanja = float(input("Masukkan total belanja: Rp"))
    kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

    # Variabel untuk diskon
    diskon = 0

    # Cek apakah pembeli memiliki kartu member
    if kartu_member == "ya":
        diskon += 15  
    
    # Cek total belanja
    if total_belanja > 500000:
        diskon += 10  
    
    # menghitung diskon
    total_diskon = (diskon / 100) * total_belanja
    total_keseluruhan= total_belanja - total_diskon

    
    print("Detail Pembelian")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang Didapatkan: {diskon}%")
    print(f"Total Harga Sebelum Diskon: Rp{total_belanja}")
    print(f"Total Harga Setelah Diskon: Rp{total_keseluruhan}")