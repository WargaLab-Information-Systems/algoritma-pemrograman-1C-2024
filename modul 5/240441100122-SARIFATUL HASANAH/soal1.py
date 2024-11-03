def calculate_discount(total_belanja, keanggotaan):
    diskon_kartu = 0
    tambahan_diskon = 0
    
    if keanggotaan == 'Gold':
        diskon_kartu = 0.15 
    elif keanggotaan == 'Silver':
        diskon_kartu = 0.10  
    elif keanggotaan == 'Bronze':
        diskon_kartu = 0.05 


    total_diskon_keanggotaan = total_belanja * diskon_kartu
    
    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05  
    
    total_diskon = total_diskon_keanggotaan + tambahan_diskon

    jumlah = total_belanja - total_diskon

    persen_diskon = (total_diskon / total_belanja) * 100
    return total_diskon, jumlah, persen_diskon

print("Selamat datang di Supermarket Sarifa")
    
while True:
        nama_pembeli = input("\nMasukkan nama pembeli : ")
        total_belanja = int(input("Masukkan total belanja (Rp): "))
        keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze) atau ketik 'Tidak' jika tidak memiliki keanggotaan: ")

        
        total_diskon, jumlah, persen_diskon = calculate_discount(total_belanja, keanggotaan)

        print(f"\nNama Pembeli: {nama_pembeli}")
        print(f"Total Belanja Sebelum Diskon: {total_belanja}")
        print(f"Diskon yang didapat: Rp {int(total_diskon)} ({int(persen_diskon)}%)")
        print(f"Total setelah diskon: Rp {int(jumlah)}")


        lagi = input("\nApakah Anda ingin memasukkan data pembeli lain? (ya/tidak): ")
        if lagi.lower() != 'ya':
            print("Terima kasih! Selamat berbelanja.")
            break


