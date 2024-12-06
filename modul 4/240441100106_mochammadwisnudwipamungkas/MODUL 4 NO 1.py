# input karakter
while True:
    karakter = input("Masukkan karakter 'X' atau 'O': ")
    if karakter == 'X' or karakter == 'O':
        break
    else:
        print("Input tidak valid, harap masukkan karakter 'X' atau 'O'")

# Meminta input ukuran sisi belah ketupat
ukuran_sisi = int(input("Masukkan ukuran sisi belah ketupat: "))

# Menghitung jumlah baris untuk belah ketupat
total_baris = 2 * ukuran_sisi - 1

for i in range(total_baris):
    # Menentukan jumlah spasi
    if i < ukuran_sisi:
        spaces = ukuran_sisi - i - 1
    else:
        spaces = i - ukuran_sisi + 1

    # Mencetak spasi
    print(' ' * spaces, end='')

    # Mencetak pola
    for j in range(2 * (ukuran_sisi - spaces) - 1):
        if (j % 2 == 0):
            print(karakter, end='')
        else:
            print(' ', end='')

    print()  # Pindah ke baris berikutnya
