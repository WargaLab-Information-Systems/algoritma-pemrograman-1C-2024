angka = int(input("Masukkan ukuran: "))
bentuk = input("Masukkan bentuk (misal: X/O): ")

# Bagian atas
for i in range(angka):
    print(' ' * (angka - i - 1) + (bentuk + ' ') * (i + 1))

# Bagian bawah
for i in range(angka - 1):
    print(' ' * (i + 1) + (bentuk + ' ') * (angka-i-1))