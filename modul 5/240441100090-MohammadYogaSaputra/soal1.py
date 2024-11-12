def hitung_diskon():
    total_belanja = int(input("Masukkan total belanja Anda: "))
    membership = input("Membership apa yang Anda miliki (gold/silver/bronze)? ").lower()

    # Diskon berdasarkan keanggotaan
    if membership == "gold":
        diskon = 0.15
        print("Anda mendapatkan diskon 15%")
    elif membership == "silver":
        diskon = 0.10
        print("Anda mendapatkan diskon 10%")
    elif membership == "bronze":
        diskon = 0.05
        print("Anda mendapatkan diskon 5%")
    else:
        diskon = 0.0
        print("Anda tidak memiliki diskon membership.")

    # Hitung diskon awal
    total_diskon = total_belanja * diskon
    print("Diskon awal berdasarkan membership: Rp", total_diskon)

    # Tambahan diskon jika totl belanja lebih dari 1 juta
    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05
        total_diskon += tambahan_diskon
        print("Anda mendapatkan tambahan diskon 5% karena belanja melebihi 1 juta")

    # Hitung total harga setelah diskon
    total_harga_setelah_diskon = total_belanja - total_diskon

    print("Total belanja setelah semua diskon: Rp", total_harga_setelah_diskon)
    return total_harga_setelah_diskon
hitung_diskon()
