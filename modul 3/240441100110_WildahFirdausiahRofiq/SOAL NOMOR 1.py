size = int(input("Masukkan ukuran: "))

# Cetak angka 1 pertama
for i in range(size):
    print(' ' * (size - 4) + 'x')

print()  # Line break

# Cetak angka 1 kedua
for i in range(size):
    print(' ' * (size - 4) + 'x')

print()  # Line break

# Cetak angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print('x' * size)
    else:
        print('x' + ' ' * (size-2)+'x')