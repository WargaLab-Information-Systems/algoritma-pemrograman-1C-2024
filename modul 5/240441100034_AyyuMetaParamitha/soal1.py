total_belanja = int(input("masukkan total belanja : "))
keanggotaan = input("member : ")

def calculate_discount(total_belanja, keanggotaan):
    # Inisialisasi diskon
    diskon = 0

    # Tentukan diskon berdasarkan jenis keanggotaan
    if keanggotaan == "Gold": 
        diskon = 0.15  # 15%
    elif keanggotaan == "Silver":
        diskon = 0.10  # 10%
    elif keanggotaan == "Bronze":
        diskon = 0.05  # 5%
    else:
        diskon = 0.0   # Tidak ada keanggotaan yang valid

    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05  # Tambahan 5%

    # Hitung total diskon
    total_diskon = total_belanja * diskon
    return total_diskon

diskon = calculate_discount(total_belanja, keanggotaan)
print(f"Total diskon yang didapat: {diskon}")

