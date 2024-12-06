n = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter pilihan (misal 'X' atau 'O'): ")
while karakter not in ['X', 'O']:
    print("karakter tidak valid. Silahkan masukkan 'X' atau 'O': ")
    karakter= input("Masukkan karakter pilihan ('X' atau 'O'): ")
# Bagian atas belah ketupat
for i in range(n):
    # Mencetak spasi
    print(' ' * (n - i - 1), end='')
    
    # Mencetak karakter
    print(karakter * (2 * i + 1))

# Bagian bawah belah ketupat
for i in range(n - 2, -1, -1):  
    # Mencetak spasi
    print(' ' * (n - i - 1), end='')
    
    # Mencetak karakter
    print(karakter * (2 * i + 1))
