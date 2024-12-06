# Fungsi untuk menghitung diskon
def calculate_discount(total_belanja, keanggotaan):
    # Diskon berdasarkan jenis keanggotaan
    diskon_keanggotaan = {
        'gold': 0.15,
        'silver': 0.10,
        'bronze': 0.05
    }
    
    # Inisialisasi diskon awal
    diskon = 0.0
    
    # Loop untuk menentukan diskon keanggotaan (dinamis)
    for jenis, nilai_diskon in diskon_keanggotaan.items():
        if keanggotaan.lower() == jenis:
            diskon = nilai_diskon
            break

    # Tambahkan diskon tambahan jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05

    # Hitung total diskon
    total_diskon = total_belanja * diskon
    # Hitung harga akhir setelah diskon
    harga_akhir = total_belanja - total_diskon

    return harga_akhir, total_diskon

# Fungsi utama untuk menjalankan program
def main():
    # Meminta input dari pengguna
    total_belanja = float(input("Masukkan total belanja pelanggan: "))
    keanggotaan = input("Masukkan jenis keanggotaan pelanggan (Gold/Silver/Bronze/Tidak ada): ")

    # Memanggil fungsi calculate_discount
    harga_akhir, total_diskon = calculate_discount(total_belanja, keanggotaan)
    
    # Menampilkan hasil
    print(f"Harga akhir: {harga_akhir}")
    print(f"Total diskon: {total_diskon}")

# Menjalankan program
main()