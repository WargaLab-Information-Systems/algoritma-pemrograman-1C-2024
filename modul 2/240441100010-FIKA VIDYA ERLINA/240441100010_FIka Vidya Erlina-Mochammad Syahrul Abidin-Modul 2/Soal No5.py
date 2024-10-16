# Input data pembeli
nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

# Cek usia
if usia < 18:
    print("Maaf usia anda belum mencukupi")
else:
    total_belanja = int(input("Masukkan total belanja: Rp"))
    member = input("Apakah Anda memiliki kartu member? (Ya/Tidak): ")

    diskon= 0
    
    #cek member
    if member == "Ya":
        diskon += 15 # diskon 15% untuk member
    #cek total belanja
    if total_belanja > 500000:
        diskon += 10 # diskon 10% untuk belanja lebih dari Rp500.000
        
    #diskon yang didapat
    Total_diskon= total_belanja*(diskon/100)

    #Harga setelah diskon
    Total_setelah_diskon= total_belanja-Total_diskon
    
    # Tampilkan hasil
    print("---Rincian Pembelian---")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Total Harga Sebelum Diskon: Rp{total_belanja}")
    print(f"Diskon yang Didapatkan: {diskon * 100}%")
    print(f"total diskon: Rp{Total_diskon}")
    print(f"Total Harga Setelah Diskon: Rp{Total_setelah_diskon}")