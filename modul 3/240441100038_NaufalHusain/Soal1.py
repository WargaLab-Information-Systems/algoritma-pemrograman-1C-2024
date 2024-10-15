# Meminta pengguna untuk memasukkan ukuran
size = int(input("Masukkan Size: "))

# Mencetak angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print('x' * size)
    else:
        
        print('x' + ' ' * (size - 2) + 'x')

print() 

# Mencetak angka 3
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print('h' * size)
    else:
        print(' ' * (size - 1) + 'n')

print()  

# Mencetak angka 8
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print('x' * size)
    else:
        print('x' + ' ' * (size - 2) + 'x')