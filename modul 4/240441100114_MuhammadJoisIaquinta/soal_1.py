angka = int(input("masukkan ukuran: "))
bentuk = input("masukkan bentuk (X/O): ").upper()

# while bentuk not in ['X', 'O']:
#     print("Not valid! Masukkan hanya 'X' atau 'O'.")
#     bentuk = input("masukkan bentuk (X/O): ").upper()

for i in range(1, angka + 1):
    for j in range(angka - i):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print(bentuk, end="   ")
    print()

for bawah in range(1, angka + 1):
    for k in range(1, bawah + 1):
        print(' ', end=" ")
    for J in range(angka - bawah):
        print(bentuk, end="   ")
    print()