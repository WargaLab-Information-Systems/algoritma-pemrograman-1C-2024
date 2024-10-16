pembeli = str(input("Masukkan Nama Anda: "))
umur = int(input("Masukkan umur Anda: "))
print(f"Nama Anda {pembeli}")
if umur >= 18:
    member = str(input("Apakah anda memiliki kartu member?(Ya/Tidak) "))
    harga = int(input("Masukkan harga barang yang anda beli: "))
    if (member == "Ya" or member == "ya") and harga >= 500000:
        print("Anda mendapatkan diskon sebesar 25%")
        print("Total harga sebelum diskon: ", harga)
        print(f"Total harga setelah diskon: {harga - (harga * 0.25)}")
    elif (member == "ya" or member == "Ya") and harga < 500000:
        print("Anda mendapatkan diskon sebesar 15%")
        print("Total harga sebelum diskon: ", harga)
        print(f"Total harga setelah diskon: {harga - (harga - 0.15)}")
    elif (member != "Ya" or member != "ya") and harga >= 500000:
        print("Anda mendapatkan diskon sebesar 10%")
        print("Total harga sebelum diskon: ", harga)
        print(f"Total harga setelah diskon: {harga - (harga - 0.10)}")
    else:
        print("Anda tidak mendapatkan diskon")
        print(f"Total harga: {harga}")
else:
    print("Maaf usia anda belum mencukupi")