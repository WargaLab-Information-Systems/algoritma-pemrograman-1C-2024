total_belanja = int(input("masukkan total belanja:"))
keanggotaan = input("masukkan keanggotaan(gold/silver/bronze/tidak ada):")

def calculate_discount(total_belanja, jenis_keanggotaan):
    #diskon berdasarkan jenis keanggotaan
    if jenis_keanggotaan == 'gold' :
        diskon_anggota = 0.15 
    elif jenis_keanggotaan == 'silver':
        diskon_anggota = 0.10 
    elif jenis_keanggotaan == 'bronze':
        diskon_anggota = 0.05 
    else:
        diskon_anggota = 0.0

    #tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon_anggota += 0.05 
    
    #hitung total diskon
    total_diskon = diskon_anggota
    total_diskon_belanja = int(total_belanja * total_diskon)
    total_bayar = int (total_belanja - total_diskon_belanja)

    print(f"Diskon yang di dapat: {total_diskon}")
    print(f"Total_diskon: Rp {total_diskon_belanja}")
    print(f"Harga setelah diskon:{total_bayar}")
    return

calculate_discount(total_belanja, keanggotaan)