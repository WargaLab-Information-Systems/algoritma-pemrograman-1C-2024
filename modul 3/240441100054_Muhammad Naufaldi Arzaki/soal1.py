size = 5  # Ukuran untuk tinggi dan lebar angka

# Angka 0
for i in range(size):
    for j in range(size):
        if (i == 0 or i == size - 1) or (j == 0 or j == size - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()  # Memberi jarak antar angka

# Angka 5
for i in range(size):
    for j in range(size):
        if (i == 0 or i == size // 2 or i == size - 1) or (j == 0 and i < size // 2) or (j == size - 1 and i > size // 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()  # Memberi jarak antar angka

# Angka 4
for i in range(size):
    for j in range(size):
        if (j == size - 1) or (i == size // 2) or (j == 0 and i < size // 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 
