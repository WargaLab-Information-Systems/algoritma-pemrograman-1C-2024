# Input untuk nama pembeli dan usia 
nama_pembeli = input("Masukkan nama pembeli: ") 
usia = int(input("Masukkan usia pembeli: ")) 
 
# Cek usia 
if  usia >= 100:
    print("usia tidak sesuai") 
elif usia <= 18:
    print ("Maaf, usia anda belum mencukupi.")
else: 
    total_harga = float(input("Masukkan total belanja: Rp ")) 
    member = input("Apakah anda memiliki kartu member (ya/tidak)?").lower() 

    diskon = 0
    if member == 'ya': 
        diskon = 15 
    elif total_harga > 500000:
        diskon = 10
 
    # Hitung total harga setelah diskon 
    total_setelah_diskon = total_harga - (total_harga * diskon / 100) 
 
    # Tampilkan hasil 
    print(f"\nNama Pembeli: {nama_pembeli}") 
    print(f"Diskon yang didapatkan: {diskon}%") 
    print(f"Total harga sebelum diskon: Rp {total_harga:.2f}") 
    print(f"Total harga setelah diskon: Rp {total_setelah_diskon:.2f}")
