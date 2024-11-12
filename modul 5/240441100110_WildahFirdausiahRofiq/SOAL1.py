def calculate_discount(total_belanja, keanggotaan):
    # Menghitung diskon berdasarkan jenis keanggotaan
    if keanggotaan == "Gold":
        diskon = 0.15
    elif keanggotaan == "Silver":
        diskon = 0.10
    elif keanggotaan == "Bronze":
        diskon = 0.05
    else:
        diskon = 0.0

    # Menambahkan diskon tambahan jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon = 0.05

    # Menghitung total diskon
    jumlah_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - jumlah_diskon

    return total_setelah_diskon, jumlah_diskon

# Meminta input dari pengguna
total_belanja = int(input("Masukkan total belanja Anda: "))
keanggotaan = input("Masukkan jenis keanggotaan Anda (Gold, Silver, Bronze, atau Tidak ada): ")

# Memanggil fungsi dan mencetak hasil
total_setelah_diskon, jumlah_diskon = calculate_discount(total_belanja, keanggotaan)
print(f"Diskon yang Anda dapatkan: {jumlah_diskon}")
print(f"Total yang harus Anda bayar setelah diskon: {total_setelah_diskon}")
