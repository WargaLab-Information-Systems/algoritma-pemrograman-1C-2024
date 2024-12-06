def hitung_diskon(total_belanja, keanggotaan):
  diskon_keanggotaan = {"gold": 0.15, "silver": 0.10, "bronze": 0.05}
  diskon_tambahan = 0.05 if total_belanja > 1000000 else 0
  
  # Menggunakan metode get() untuk mengambil diskon berdasarkan keanggotaan
  diskon = diskon_keanggotaan.get(keanggotaan.lower(), 0) + diskon_tambahan

  total_bayar = total_belanja * (1 - diskon)
  return total_bayar, diskon * 100

# Meminta input pengguna
total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold, Silver, Bronze, tidak ada): ").lower()

# Disini Memanggil fungsi dan mencetak hasil
total_bayar, diskon = hitung_diskon(total_belanja, keanggotaan)
print(f"Total bayar setelah diskon: Rp{total_bayar:,.2f}")
print(f"Anda mendapatkan diskon sebesar {diskon:.2f}%")