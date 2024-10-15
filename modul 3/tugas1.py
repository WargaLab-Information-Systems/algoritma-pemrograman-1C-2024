size = int(input("masukkan size : "))

# Membuat angka 0
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size - 1 or ii == 0 or ii == size - 1:
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print()

# Membuat angka 0
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size - 1 or ii == 0 or ii == size - 1:
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print()

# Membuat angka 2
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size - 1 or i == size // 2 or ii == size - 1 and i < size // 2 or ii == 0 and i > size // 2:
            print("2", end=" ")
        else:
            print(" ", end=" ")
    print()