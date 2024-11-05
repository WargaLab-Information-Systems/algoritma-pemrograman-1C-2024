total_belanja = int(input("masukkan total belanja: "))
keanggotaan = input("masukkan keanggotaan (Gold/Silver/Bronze/Tidak ada): ")

def calculate_discount(total_belanja, jenis_keanggotaan) :
    # Diskon berdasarkan jenis keanggotaan
    if jenis_keanggotaan == 'Gold':
        diskon_anggota = 0.15
    elif jenis_keanggotaan == 'Silver':
        diskon_anggota = 0.10
    elif jenis_keanggotaan == 'Bronze':
        diskon_anggota = 0.05
    else:
        diskon_anggota = 0.0
    
    # Hitung diskon keanggotaan
    diskon_keanggotaan = total_belanja*diskon_anggota
    
    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05
    else :
        tambahan_diskon = 0.0
        
    # Hitung total diskon 
    total_diskon = diskon_keanggotaan + tambahan_diskon
    
    return diskon_keanggotaan, tambahan_diskon, total_diskon

if total_belanja < 0:
    print("total belanja tidak boleh negatif")
else:
    diskon_keanggotaan, tambahan_diskon, total_diskon = calculate_discount(total_belanja, keanggotaan) 
    print(f"Diskon keanggotaan: Rp {diskon_keanggotaan}")
    print(f"Tambahan diskon (jika belanja > Rp1,000,000): Rp {tambahan_diskon}")
    print(f"total diskon yang didapat: Rp {total_diskon}")
    print(f"total setelah diskon: Rp{total_belanja - total_diskon}")
    

