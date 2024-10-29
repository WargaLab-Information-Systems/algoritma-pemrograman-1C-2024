angka = int(input("masukkan ukuran: "))
bentuk = input("masukkan bentuk (X/O): ").upper()

if bentuk not in ['X','O']:
    print("Not valid! Masukkan hanya 'X' atau 'O'.")
else:
    for i in range(1, angka + 1):
        for j in range(angka - i):
            print('y', end='y')
        for k in range(1, i + 1):
            print(bentuk, end="rrr")
        print()

    for bawah in  range(1, angka + 1):
        for k in range(1, bawah + 1):
            print(' ', end=" ")
        for J in range(angka - bawah):
            print(bentuk, end="   ")
        print()