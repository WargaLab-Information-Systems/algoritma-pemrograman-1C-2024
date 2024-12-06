def calculate_discount(total, keanggotaan) :
    if keanggotaan == "Gold":
        diskon_keanggotaan = 0.15
    elif keanggotaan == "Silver":
        diskon_keanggotaan = 0.10
    elif keanggotaan == "Bronze":
        diskon_keanggotaan = 0.05
    elif keanggotaan == "None":
        diskon_keanggotaan = 0.0
    
    diskon_total = 0.05 if total > 1000000 else 0.0

    # total diskon yang didapatkan
    total_diskon_tambahan_rupiah = total * diskon_total
    total_diskon_rupiah = total * diskon_keanggotaan

    # total yang harus dibayar 
    total_akhir = total - total_diskon_rupiah
    return total_diskon_rupiah, total_diskon_tambahan_rupiah, total_akhir

# output
print("--- Selamat Datang di Supermarket Ormos! ---")
print()
total = float(input("Masukkan Total Belanja:"))

while True:
    keanggotaan = input("Masukkan Jenis Keanggotaan (Gold, Silver, Bronze, None)")
    if keanggotaan in ["Gold", "Silver", "Bronze", "None"]:
        break
    else:
        print("Silahkan masukkan salah satu dari keanggotaan di atas.")

total_diskon_rupiah, total_diskon_tambahan_rupiah, total_akhir = calculate_discount(total, keanggotaan)
print(f"Diskon Keanggotaan: {total_diskon_rupiah:,}")
print(f"Diskon Tambahan: {total_diskon_tambahan_rupiah:,}")
print(f"Total Belanja: {total_akhir:,}")