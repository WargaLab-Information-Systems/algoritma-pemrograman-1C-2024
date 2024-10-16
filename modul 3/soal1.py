# NIM akhir adalah 034

# program angka 0
size = 5  # Mengatur jumlah baris dan kolom

for i in range(1, size+1):
    for j in range(1, size+1):
        if i == 1 or i == size or j == 1 or j == size:
            print("#", end="")
        else:
            print(" ", end="")
    print()


# program untuk angka 3
# Input ukuran
size = 5

if size :
    # Cetak baris atas
    print("*" * size)
    
    # Cetak sisi kanan atas
    for _ in range(size // 2 - 1):
        print(" " * (size - 1) + "*")
    
    # Cetak baris tengah
    print("*" * size)
    
    # Cetak sisi kanan bawah
    for _ in range(size // 2 - 1):
        print(" " * (size - 1) + "*")
    
    # Cetak baris bawah
    print("*" * size)
else:
    print()

# program untuk angka 4

size = 5
for i in range(size):
    if i == size // 2:
        print("x" * size)
    elif i < size // 2:
        print("x" + " " * (size - 2) + "x")
    else:
        print(" " * (size-1) + "x")