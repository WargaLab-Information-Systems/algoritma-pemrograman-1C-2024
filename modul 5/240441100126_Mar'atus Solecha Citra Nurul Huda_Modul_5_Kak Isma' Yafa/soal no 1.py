def calculate_discount(total_belanja, membership):
    # Diskon berdasarkan jenis keanggotaan
    if membership.lower() == "gold":
        discount_rate = 0.15
    elif membership.lower() == "silver":
        discount_rate = 0.10
    elif membership.lower() == "bronze":
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        discount_rate += 0.05

    # Menghitung total diskon
    total_discount = total_belanja * discount_rate
    return total_discount

# Meminta input dari pengguna:
total_belanja = float(input("Masukkan total belanja: Rp"))
membership = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ")

if total_belanja < 0:
    print("Total belanja tidak boleh negatif.")
else:
    discount = calculate_discount(total_belanja, membership)
    total_setelah_diskon = total_belanja - discount
    print(f"Diskon yang didapat: Rp{discount}")
    print(f"Total setelah diskon: Rp{total_setelah_diskon}")