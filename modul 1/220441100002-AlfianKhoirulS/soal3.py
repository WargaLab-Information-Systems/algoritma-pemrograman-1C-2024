# Program Konversi Mata Uang USD ke IDR

# Input: Jumlah uang dalam USD dan nilai kurs pada tanggal tertentu
usd = float(input("Masukkan jumlah uang dalam USD: "))  # Input jumlah USD yang ingin dikonversi
kurs_idr = input("Masukkan nilai kurs USD ke IDR: ")  # Input kurs 1 USD ke IDR 15.104 Menurut viva.co,id

# Menghapus koma dari input kurs jika ada
kurs_idr = kurs_idr.replace(",", "")

# Konversi kurs ke tipe float
kurs_idr = float(kurs_idr)

# Proses: Menghitung konversi ke Rupiah
jumlah_idr = usd * kurs_idr

# Output: Menampilkan jumlah uang dalam Rupiah
print(f"Jumlah Rupiah yang didapatkan: {jumlah_idr:,.2f} IDR")
