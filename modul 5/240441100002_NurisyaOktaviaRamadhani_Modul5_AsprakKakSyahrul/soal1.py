def calculate_discount(total_belanja, keanggotaan):
    if keanggotaan == 'Gold':
        diskon_keanggotaan = 0.15
    elif keanggotaan == 'Silver':
        diskon_keanggotaan = 0.10
    elif keanggotaan == 'Bronze':
        diskon_keanggotaan = 0.05
    else:
        diskon_keanggotaan = 0.0
    jumlah_diskon_keanggotaan = total_belanja * diskon_keanggotaan
    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05
    else:
        tambahan_diskon = 0.0
    total_diskon = jumlah_diskon_keanggotaan + tambahan_diskon
    total_setelah_diskon = total_belanja - total_diskon
    return total_setelah_diskon, jumlah_diskon_keanggotaan, tambahan_diskon, total_diskon
total_belanja = float(input("Masukkan total belanja: Rp "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak Ada): ")
total_setelah_diskon, jumlah_diskon_keanggotaan, tambahan_diskon, total_diskon = calculate_discount(total_belanja, keanggotaan)
print(f"Diskon Keanggotaan: Rp {jumlah_diskon_keanggotaan}")
print(f"Diskon Tambahan: Rp {tambahan_diskon}")
print(f"Total Diskon: Rp {total_diskon}")
print(f"Total Setelah Diskon: Rp {total_setelah_diskon}")