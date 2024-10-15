nama = input("nama pembeli :")
usia = int(input("usia pembeli:"))
total_belanja = int(input("total belanja:"))
member = input("apakah pembeli memiliki member? iya/tidak : ")
if member == "iya":
    member = True
else :
    member = False

if usia < 18:
    print("maaf usia belum mencukupi")
    exit()
else:
    diskon = 0
    if member:
        diskon += 15
    
    if total_belanja >= 500000:
        diskon = 10
        
diskon_rupiah = total_belanja * diskon/100
total_bayar = total_belanja - diskon_rupiah

print("nama pembeli:", nama)
print("diskon harga yang didapatkan:", diskon, "%")
print("total harga sebelum diskon, :", total_belanja)
print("total harga setelah diskon :", total_bayar)