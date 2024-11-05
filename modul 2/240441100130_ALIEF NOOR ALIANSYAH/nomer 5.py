# Input untuk nama pembeli dan usia
nama_pembeli = input("Masukkan nama pembeli: ") 
usia = int(input("Masukkan usia pembeli: ")) 
 
# Cek usia 
if usia < 18: 
    print("Maaf, usia anda belum mencukupi.") 
else: 
    # Input total harga 
    harga = int(input("Masukkan total belanja: Rp ")) 
    member = input("Apakah anda memiliki kartu member (ya/tidak)? ")
 
    # Cek diskon 
    diskon = 0 
    if member == 'ya' and harga >= 500000:
        diskon += 25 
    elif member == 'ya': 
        diskon += 15
    elif harga >= 500000: 
        diskon += 10
    else:
        print("Tidak dapat diskon")


 
    # Hitung total harga setelah diskon 
    total_setelah_diskon = harga - (harga * diskon / 100) 

    # Tampilkan hasil 
    print("Nama Pembeli: ",nama_pembeli) 
    print("Diskon yang didapatkan: %",diskon) 
    print("Total harga sebelum diskon: Rp ",harga) 
    print("Total harga setelah diskon: Rp ",total_setelah_diskon)  
