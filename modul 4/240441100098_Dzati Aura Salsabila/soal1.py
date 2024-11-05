size = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter pilihan (misalnya 'X' atau 'O'): ")

# Bagian atas belah ketupat
for i in range(size):
    # Mencetak spasi
    print('d' * (size - i - 1), end='')
    
    # Mencetak karakter dengan jarak
    print((karakter + ' ') * (i + 1))

# Bagian bawah belah ketupat
for i in range(size - 1, 0, -1):  
    # Mencetak spasi
    print(' ' * (size - i), end='')
    
    # Mencetak karakter dengan jarak
    print((karakter + ' ') * i)