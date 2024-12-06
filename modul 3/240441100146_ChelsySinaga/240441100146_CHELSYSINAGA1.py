# Meminta input ukuran size
size = int(input("Masukan Size (harus lebih dari 5): "))

# Mengecek jika size kurang dari 5
if size <5 :
    print("Size harus lebih dari 5.")
else:
    # Cetak angka 1
    for i in range(size):
        if i == 0 or i == size - 1:
            print(" " * (size-1) + "x")
        else:
            print(" " * (size-1) + "x")
    print()

    # Cetak angka 4
    for i in range(size):
        if i == size // 2:
            print("x" * size)
        elif i < size // 2:
            print("x" + " " * (size // 2 - 1) + "x")
        else:
            print(" " * (size // 2) + "x")
    print()

     # Cetak angka 6
    for i in range(size):
        if i == 0 or i == size // 2 or i == size-1:
            print("x" * size)
        elif i < size //2:
            print("x")
        else:
            print("x" + " " * (size-2) + "x")
    print()