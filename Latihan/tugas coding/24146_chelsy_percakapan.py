karakter1 = "chelsi"
karakter2 = "Dina"

print(f"{karakter1}: Hai {karakter2}, bagaimana kabarmu?")
print(f"{karakter2}: Hai {karakter1}, kabarku baik. Bagaimana denganmu?")
print(f"{karakter1}: Aku juga baik. Eh, aku sedang mencoba menghitung sesuatu.")

print(f"{karakter2}: Wah, apa yang sedang kamu hitung?")
print(f"{karakter1}: Aku sedang menghitung berapa total uang yang akan aku punya jika aku menabung setiap bulan.")

tabungan_bulanan = float(input(f"{karakter2}: Berapa jumlah tabungan per bulan yang kamu simpan? "))
jumlah_bulan = int(input(f"{karakter2}: Berapa bulan kamu akan menabung? "))

# Operasi Aritmatika: Menghitung total tabungan setelah beberapa bulan
total_tabungan = tabungan_bulanan * jumlah_bulan

print(f"{karakter2}: Jadi, setelah menabung selama {jumlah_bulan} bulan, kamu akan memiliki total {total_tabungan:.2f}.")

# Operasi Logika: Menentukan apakah total tabungan cukup untuk membeli sesuatu
harga_barang = float(input(f"{karakter2}: Berapa harga barang yang ingin kamu beli? "))

if total_tabungan >= harga_barang:
    sisa_uang = total_tabungan - harga_barang
    print(f"{karakter2}: Wah, kamu punya cukup uang untuk membeli barang tersebut. Setelah membelinya, kamu masih punya sisa uang sebesar {sisa_uang:.2f}.")
else:
    kekurangan = harga_barang - total_tabungan
    print(f"{karakter2}: Sayangnya, uangmu belum cukup. Kamu kekurangan {kekurangan:.2f} untuk membeli barang tersebut.")

# Diskusi tentang rencana menabung lebih banyak
print(f"{karakter1}: Kalau aku menabung lebih banyak setiap bulan, berapa lama aku bisa mencapai target?")
tabungan_baru = float(input(f"{karakter2}: Berapa jumlah tabungan yang akan kamu simpan setiap bulan mulai sekarang? "))

# Operasi Aritmatika: Menghitung jumlah bulan baru untuk mencapai target
jumlah_bulan_baru = harga_barang / tabungan_baru

print(f"{karakter2}: Dengan menabung {tabungan_baru:.2f} per bulan, kamu akan mencapai target setelah {jumlah_bulan_baru:.1f} bulan.")

# Mengakhiri percakapan
print(f"{karakter1}: Terima kasih atas sarannya, {karakter2}. Aku akan mulai menabung lebih banyak.")
print(f"{karakter2}: Sama-sama, {karakter1}. Semoga berhasil dengan rencana menabungmu!")
