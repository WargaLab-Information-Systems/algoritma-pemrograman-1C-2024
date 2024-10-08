nama = input("masukkan nama: ")
umur = int(input("masukkan umur: "))

if umur <18:
    print("Maaf usia anda belum mencukupi")
    exit()
else:
    total_harga= int(input("masukkan total belanja: "))
    kartu_member= input("apakah anda punya kartu member?(ya/tidak)")
    if kartu_member =="ya":
       diskon_member=15 
    else:
       diskon_member=0
    if total_harga >500000:
        diskon_total_harga=10
    else:
        diskon_total_harga=0
           

total_diskon = diskon_member + diskon_total_harga
jumlah_diskon = total_harga * (total_diskon / 100)
total_setelah_diskon = total_harga - jumlah_diskon


print("Nama Pembeli:" ,nama)
print("Diskon yang didapatkan:" ,total_diskon,"%")
print("Total harga sebelum diskon: Rp" ,total_harga, )
print("Jumlah Diskon: Rp",jumlah_diskon)
print("Total harga setelah diskon: Rp",total_setelah_diskon)