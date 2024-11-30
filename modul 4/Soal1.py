size = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter pilihan (misalnya 'X' atau 'O'): ")
while karakter not in ['X', 'O']:
    print("karakter tidak valid. Silahkan masukkan 'x' atau 'o': ")
    karakter= input("Masukkan karakter pilihan('x'atau'o'): ")
# Bagian atas belah ketupat
for i in range(size):
    # Mencetak spasi
    print(' ' * (size - i - 1), end='')
    
    # Mencetak karakter
    print(karakter * (2 * i + 1))

# Bagian bawah belah ketupat
for i in range(size - 2, -1, -1):  
    # Mencetak spasi
    print(' ' * (size - i - 1), end='')
    
    # Mencetak karakter
    print(karakter*(2*i+1))
    