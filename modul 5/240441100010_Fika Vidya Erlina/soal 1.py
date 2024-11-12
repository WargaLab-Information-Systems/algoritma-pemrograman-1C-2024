def super_market():
    belanja = int(input("Masukkan total belanja: "))
    member = input("Apa keanggotaan anda (gold/silver/bronze/tidak ada): ")
    
    # Diskon berdasarkan keanggotaan
    if member == "gold":
        diskon_keanggotaan = 15
    elif member == "silver":
        diskon_keanggotaan = 10
    elif member == "bronze":
        diskon_keanggotaan = 5
    else:
        diskon_keanggotaan = 0

    # Menentukan diskon tambahan
    diskon_tambahan = 0
    if belanja > 1000000:
        diskon_tambahan = 5

    # Menghitung total diskon
    total_diskon_persen = diskon_keanggotaan + diskon_tambahan
    total_diskon_keanggotaan = int(belanja * diskon_keanggotaan / 100)
    total_diskon_tambahan = int(belanja * diskon_tambahan / 100)
    total_diskon = int(belanja * total_diskon_persen / 100)
    total_bayar = int(belanja - total_diskon)
    
    print("Diskon Keanggotaan: ", diskon_keanggotaan, "%" , "Rp", total_diskon_keanggotaan, )
    print("diskon tambahan: ", diskon_tambahan, "%", "Rp", total_diskon_tambahan, )
    print("Total Diskon: Rp", total_diskon)
    print("Harga Setelah Diskon: Rp", total_bayar)
    
    return total_bayar

print(super_market())