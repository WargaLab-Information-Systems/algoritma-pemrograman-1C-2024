def calculate_discound():
    total_belanja = int(input("Masukkan total_belanja: "))
    jenis_keanggotaan = input("Apa keanggotaan anda (gold/silver/bronze/tidak ada): ").lower()
    
    # Diskon berdasarkan keanggotaan
    if jenis_keanggotaan == "gold":
        diskon_keanggotaan = 15
    elif jenis_keanggotaan == "silver":
        diskon_keanggotaan = 10
    elif jenis_keanggotaan == "bronze":
        diskon_keanggotaan = 5
    else:
        diskon_keanggotaan = 0

    # Menentukan diskon tambahan
    diskon_tambahan = 0
    if total_belanja > 1000000:
        diskon_tambahan = 5

    # Menghitung total diskon
    total_diskon_persen = diskon_keanggotaan + diskon_tambahan
    total_diskon = total_belanja * total_diskon_persen / 100
    total_bayar = total_belanja - total_diskon
    
    print("Diskon yang didapat:", total_diskon_persen, "%")
    print("Total Diskon: Rp", total_diskon)
    print("Harga Setelah Diskon: Rp", total_bayar)
(calculate_discound())