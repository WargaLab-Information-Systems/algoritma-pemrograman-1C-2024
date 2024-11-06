N = int(input("Masukkan ukuran sisi belah ketupat (N): "))
karakter = input("Masukkan karakter pilihan ('X' atau 'O'): ")
while karakter not in ['X', 'O']:
    print("Karakter tidak valid. Silakan masukkan 'X' atau 'O'.")
    karakter = input("Masukkan karakter pilihan ('X' atau 'O'): ")
for i in range(N):
    print('  ' * (N - i - 1), end=' ')
    for j in range(2 * i + 1):
        print(karakter, end=' ')
    print()  
for i in range(N - 2, -1, -1):
    print('  ' * (N - i - 1), end=' ')
    for j in range(2 * i + 1):
        print(karakter, end=' ')
    print()