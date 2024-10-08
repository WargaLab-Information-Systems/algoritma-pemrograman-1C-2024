Nama_pembeli = str(input("masukkan nama Anda : "))
usia =  int(input("masukkan usia Anda : "))

# membuat penyeleksian kondisi
if usia < 18:
    print("maaf usia anda tidak mencukupi")
else:
    total_belanja = int(input("masukkan total belanja anda (Rp): "))
    member = input("apakah anda mempunyai member ? ya / tidak : ") == "tidak"

    diskon = 0
    
    if member == "ya":
        diskon = 0.15 # 15% dari 15 dibagi 100 hasilnya 0,15, ini jika memiliki member
    elif total_belanja >= 500000:
        diskon = 0.10 # 10% jika tidak memiliki member tetapi total belanja diatas 50000
    
    
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    print("Nama pembeli adalah", Nama_pembeli)
    print("diskon yang didapat :", int(diskon * 100),"%")
    print("Total harga sebelum diskon : ", int(total_belanja))
    print("Total harga setelah diskon : ", int(total_setelah_diskon))