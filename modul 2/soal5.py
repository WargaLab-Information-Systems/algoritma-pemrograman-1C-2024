nama = input("Nama pembeli:")
usia = int(input("Usia pembeli:"))
total_belanja = int(input("Total belanja Rp :"))
member = input("Apakah pembeli memiliki member?(Ya/Tidak)")
if usia <18 :
    print("Maaf usia belum mencukupi")
    exit()
else :
    diskon = 0
    if member:
        diskon += 15
        "Iya"
    if total_belanja >= 500000:
        diskon += 10
        "Tidak"
diskon_rupiah = total_belanja * diskon/100
total_bayar = total_belanja - diskon_rupiah 

print("Nama pembeli")
print("diskon harga yang didapat:", diskon, "%")
print("total harga sebelum diskon: ", total_belanja)
print("total harga sesudah diskon:", total_bayar)