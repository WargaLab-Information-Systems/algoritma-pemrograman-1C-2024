N = int(input("Masukkan ukuran sisi belah ketupat (N): "))
karakter = input("Masukkan karakter yang diinginkan (X atau O): ")

# Bagian atas belah ketupat
for i in range(N):
    print(' ' * (N - i - 1), end='')
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(karakter, end='')
        else:
            print(' ', end='')
    print()

# Bagian bawah belah ketupat
for i in range(N - 2, -1, -1):
    print(' ' * (N - i - 1), end='')
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(karakter, end='')
        else:
            print(' ', end='')
    print()
