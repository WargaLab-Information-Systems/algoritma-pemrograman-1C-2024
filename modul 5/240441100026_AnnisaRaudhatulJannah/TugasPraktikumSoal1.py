total_belanja = int(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan keanggotaan (Gold/Silver/Bronze/Tidak ada): ")

def calculate_discount(total_belanja, jenis_keanggotaan):
  # Diskon berdasarkan jenis keanggotaan
  if jenis_keanggotaan == 'Gold':
    diskon_anggota = 0.15
  elif jenis_keanggotaan == 'Silver':
    diskon_anggota = 0.10
  elif jenis_keanggotaan == 'Bronze':
    diskon_anggota = 0.05
  else:
    diskon_anggota = 0.0

  # Tambahan diskon jika total belanja lebih dari 1 juta
  if total_belanja > 1000000:
    diskon_anggota += 0.05

  # Hitung total diskon
  total_diskon = diskon_anggota
  total_diskon_belanja = int(total_belanja * total_diskon)
  total_bayar = int (total_belanja - total_diskon_belanja)

  print(f"Diskon yang didapat {total_diskon}")
  print(f"Total Diskon: Rp {total_diskon_belanja}")
  print(f"Harga Setelah Diskon {total_bayar}")
  return total_bayar

print(calculate_discount(total_belanja, keanggotaan)) 