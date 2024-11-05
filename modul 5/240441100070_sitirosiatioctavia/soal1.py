def calculate_discount(total_belanja, keanggotaan):
    # Diskon awal berdasarkan keanggotaan
    if keanggotaan == "gold":
        diskon = 0.15
    elif keanggotaan == "silver":
        diskon = 0.10
    elif keanggotaan == "bronze":
        diskon = 0.05
    else:
        diskon = 0.0
    
    # Tambahan diskon jika total belanja lebih dari 1 juta
    tambahan_diskon = 0.05 if total_belanja > 1000000 else 0.0
    total_diskon_persen = diskon + tambahan_diskon
    
    # Menghitung total diskon
    total_diskon = total_belanja * total_diskon_persen
    harga_setelah_diskon = total_belanja - total_diskon
    
    # Menampilkan informasi diskon
    print(f"Diskon keanggotaan: {diskon*100}%")
    if tambahan_diskon > 0:
        print(f"Tambahan diskon karena belanja lebih dari 1 juta: {tambahan_diskon*100}%")
    print(f"Total diskon yang diberikan: {total_diskon_persen*100}%")
    
    return harga_setelah_diskon

# Mengambil input dari pengguna tanpa try-except
total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak Ada): ")

# Memanggil fungsi calculate_discount dan menampilkan hasil
harga_final = calculate_discount(total_belanja, keanggotaan)
print("Total yang harus dibayar setelah diskon:", harga_final)
