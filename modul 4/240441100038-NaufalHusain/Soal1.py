# program membuat bentuk belah ketupat
# Input ukuran sisi dan karakter dari pengguna
angka = int(input("Masukkan ukuran belah ketupat (N): "))
bentuk = input("Masukkan bentuk (X/O): ").upper()

if bentuk not in ['X', 'O']:
    print("Tidak valid! Masukkan hanya 'X' atau 'O'.")
else:
    # Bagian segitiga atas
    for i in range(1, angka + 1):
        for j in range(angka - i):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(bentuk, end="   ")
        print()

    # Bagian segitiga bawah
    for i in range(1, angka):
        for j in range(i):
            print(' ', end=" ")
        for k in range(angka - i):
            print(bentuk, end="   ")
        print()
