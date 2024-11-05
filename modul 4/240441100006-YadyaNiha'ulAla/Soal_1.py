n = int(input("Masukkan ukuran belah ketupat (N): "))

char = input("Masukkan karakter (Hanya X/O): ").upper()
while char != 'x' and char != 'o':
    print("Karakter tidak valid. Harap masukkan X/O.")
    char = input("Masukkan karakter (Hanya X/O): ").upper()

# atas
for i in range(n):
    print(' ' * (n - i - 1), end="")
    print(char * (2 * i + 1))

# bawah
for i in range(n-2, -1, -1):
    print(' ' * (n - i - 1), end="")
    print(char * (2 * i + 1))