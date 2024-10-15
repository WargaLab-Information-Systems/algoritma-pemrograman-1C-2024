nama = input("nama pembeli :")
usia = int(input("usia pembeli :"))
total_belanja = int(input("total belanja Rp "))
member_input = input("apakah anda memiliki kartu member? (ya/tidak) :")

if usia < 18:
    print("maaf usia belum mencukupi")
    exit ()
else :
    diskon = 0
    member = (member_input == "ya")

    if member:
        diskon = 15
    if total_belanja > 500000:
        diskon = 10
    
    total_sebelum_diskon = total_belanja
    total_setelah_diskon = total_belanja*(1-diskon/100)

print(f"\nNama pembeli: {nama} ")
print(f"diskon yang didapatkan: {diskon} ")
print(f"total harga sebelum diskon: Rp.{int(total_sebelum_diskon)}")
print(f"total harga sesudah diskon: Rp.{int(total_setelah_diskon)}")


