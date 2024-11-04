size = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter pilihan (misalnya 'X' atau 'O'): ")

# Bagian atas belah ketupat
for i in range(size):
    # Mencetak spasi
    print(' ' * (size - i - 1), end='')
    
    # Mencetak karakter
    print(karakter * (2 * i + 1))

# Bagian bawah belah ketupat
for i in range(size - 2, -1, -1): #start stop step #deretan angka 
    # Mencetak spasi
    print(' ' * (size - i - 1), end='')
    
    # Mencetak karakter
    print(karakter * (2 * i + 1))
