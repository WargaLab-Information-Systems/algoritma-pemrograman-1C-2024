# Loop untuk baris bagian atas hingga tengah
for i in range(N):
    # Cetak spasi di depan karakter untuk membuat bentuk belah ketupat
    print(' ' * (N - i - 1), end='')

    # Cetak karakter yang dipilih
    for j in range(2 * i + 1):
        print(karakter, end='')
    print()  # Pindah ke baris berikutnya

# Loop untuk baris bagian tengah ke bawah
for i in range(N - 2, -1, -1):
    # Cetak spasi di depan karakter untuk membuat bentuk belah ketupat
    print(' ' * (N - i - 1), end='')

    # Cetak karakter yang dipilih
    for j in range(2 * i + 1):
        print(karakter, end='')
    print()  # Pindah ke baris berikutnya