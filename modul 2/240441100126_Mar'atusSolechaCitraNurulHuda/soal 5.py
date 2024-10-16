# INPUT NAMA DAN USIA PEMBELI
nama_pembeli = input("masukkan nama pembeli: ")
usia = int(input("masukkan usia pembeli: "))

# CEK USIA 
if usia < 18 :
    print("maaf, usia anda belum mencukupi")
else :
    total_harga = float(input("masukkan total: Rp "))
    member = input("apakah anda memiliki kartu member? (ya/tidak)? ").lower()

    # CEK DISKON 
    diskon = 0 
    if member == 'ya' and total_harga >= 500000 :
        diskon = 25
    elif member == 'ya' :
        diskon = 10
    elif total_harga >= 500000 :
        diskon = 10 
    else :
        print("anda tidak mendapatkan diskon")

    
    total_setelah_diskon = total_harga - (total_harga * diskon / 100)

    # HASIL 
    print(f"\nnama pembeli : {nama_pembeli}")
    print(f"diskon yang didapatkan : {diskon}%")
    print(f"total harga sebelum diskon : Rp {total_harga:}")
    print(f"total harga setelah diskon : Rp {total_setelah_diskon:}")
print(f"total harga setelah diskon : Rp {total_setelah_diskon:}")