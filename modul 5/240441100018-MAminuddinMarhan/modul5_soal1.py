def calculate_discount():
    total_belanja = int(input("Masukkan jumlah harga belanjaan anda: Rp."))
    member = str(input("Apakah anda memiliki keanggotaan? Jika ada jawab (ya) "))
    diskon = 0.0
    if member == "ya":
        keanggotaan = str(input("Apa jenis keanggotaan yang anda miliki?(gold/silver/bronze) "))
        if keanggotaan == "gold":
            print("Karena anda memiliki keanggotaan Gold, maka anda mendapatkan diskon sebesar 15%")
            diskon += 0.15
            print(f"Dan dari keanggotaan Gold, anda mendapatkan potongan sebesar Rp.{total_belanja * diskon}")
        elif keanggotaan == "silver":
            print("Karena anda memiliki keanggotaan Silver, maka anda mendapatkan diskon sebesar 10%")
            diskon += 0.10
            print(f"Dan dari keanggotaan Silver, anda mendapatkan potongan sebesar Rp.{total_belanja * diskon}")
        elif keanggotaan == "bronze":
            print("Karena anda memiliki keanggotaan Bronze, maka anda mendapatkan diskon sebesar 5%")
            diskon += 0.05
            print(f"Dan dari keanggotaan Bronze, anda mendapatkan potongan sebesar Rp.{total_belanja * diskon}")
        else:
            print("Keanggotaan tidak valid, anda tidak mendapatkan diskon")
    else:
        print("Maaf anda tidak mendapatkan diskon karena tidak memiliki keanggotaan")
    if total_belanja > 1000000:
        print("Karena total belanja anda melebihi 1 juta, maka anda mendapatkan diskon sebesar 5%")
        diskon += 0.05
        print(f"Dan mendapatkan potongan sebesar Rp.{total_belanja * 0.05}")
    print(f"Jumlah total diskon yang anda dapatkan sebesar {diskon * 100}% atau mendapatkan potongan Rp.{total_belanja * diskon}")
    print(f"Dan jumlah harga belanjaan anda setelah diskon adalah Rp.{total_belanja - (total_belanja * diskon)}")
calculate_discount()