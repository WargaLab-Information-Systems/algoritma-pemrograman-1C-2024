def calculate_discount():
    total_belanja = int(input("Masukkan total belanja: "))
    membership = input("Apakah kamu mempunyai kartu membership? (iya/tidak): ").lower()
    
    # Tentukan diskon awal
    diskon = 0
    
    # Jika mempunyai membership, tentukan diskon berdasarkan kartu membership
    if membership == "iya":
        kartu = input("Pilih membership anda (Gold/Silver/Bronze): ").capitalize()
        
        if kartu == "Gold":
            diskon = 0.15
        elif kartu == "Silver":
            diskon = 0.10
        elif kartu == "Bronze":
            diskon = 0.05
        else:
            print("Harap masukkan kartu dengan benar!!!")
            return None, None  # Menghentikan program jika input kartu salah
    elif membership == "tidak":
        print("Anda tidak mendapatkan diskon")
    else:
        print("Input membership tidak valid.")
        return None, None  # Menghentikan program jika input membership tidak valid

    # Cek apakah total belanja lebih dari 1 juta untuk diskon tambahan
    if total_belanja > 1000000:
        diskon += 0.05
        print("Karena Anda berbelanja lebih dari 1 juta, maka Anda dapat diskon tambahan 5%")

    # Hitung total diskon dan total yang harus dibayar
    total_diskon = total_belanja * diskon
    after_diskon = total_belanja - total_diskon
    
    return total_diskon, after_diskon

# Panggil fungsi dan tampilkan hasilnya
total_diskon, after_diskon = calculate_discount()

if total_diskon is not None and after_diskon is not None:
    print(f"Total diskon yang didapat: Rp{total_diskon}")
    print(f"Total yang harus dibayar: Rp{after_diskon}")
