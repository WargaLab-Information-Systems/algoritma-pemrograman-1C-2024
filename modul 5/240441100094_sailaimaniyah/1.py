def calculate_discount():
    
    total_belanja= int(input("masukkan total belanja :"))
    jenis_keanggotaan= input("masukkan jenis keanggotaan :")
    diskon=0
    
    # Menentukan diskon berdasarkan jenis keanggotaan
    if jenis_keanggotaan == 'gold':
        diskon = 0.15  # 15%
    elif jenis_keanggotaan == 'silver':
        diskon = 0.10  # 10%
    elif jenis_keanggotaan == 'bronze':
        diskon = 0.05  # 5%
    else:
        diskon=0
    
    # Menambahkan diskon tambahan jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05  # Tambahan 5%
    
    # Menghitung total diskon
    total_diskon = total_belanja * diskon
    
    # Menghitung total yang harus dibayar setelah diskon
    total_setelah_diskon = total_belanja - total_diskon
    

    print("Total Diskon:",total_diskon)
    print("Total Setelah Diskon:",total_setelah_diskon)

calculate_discount()