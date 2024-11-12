# Memasukkan data pembeli
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))

# Mengecek usia pembeli
if usia_pembeli < 18:
    print("Maaf usia anda belum mencukupi")
else:
    # Memasukkan informasi tambahan
    total_belanja = float(input("Masukkan total belanja (Rp): "))
    kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

    # Menghitung diskon
    diskon_member = 0.15 if kartu_member == "ya" else 0.0
    diskon_total = 0.10 if total_belanja > 500000 else 0.0

    # Total diskon yang didapatkan
    diskon_yang_didapatkan = max(diskon_member, diskon_total)  # Mengambil diskon yang lebih besar

    # Menghitung harga setelah diskon
    total_diskon = total_belanja * diskon_yang_didapatkan
    harga_setelah_diskon = total_belanja - total_diskon

    # Menampilkan hasil
    print(f"\n--- Detail Pembelian ---")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon_yang_didapatkan * 100}%")
    print(f"Total harga sebelum diskon: Rp{total_belanja:.2f}")
    print(f"Total harga setelah diskon: Rp{harga_setelah_diskon:.2f}")
