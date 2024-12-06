size = int(input("Masukan Size (harus lebih dari 3): "))
#Mengecek size jika  dari 3
if size < 3:
    print("Size harus lebih dari 3.")
else:
    # Cetak angka 1
    for i in range(size):   # jarak untuk size
        if i < size:
            print(" " * ((size-1)//2) + "x")
    print()

    # Cetak angka 3
    for i in range(size):
        if i == 0 or i == size - 1 or i == size // 2:
            print("x" * size) 
        else:
            print(" " * (size - 1) + "x") 
    print()

    # Cetak angka 8
    for i in range(size):
        if i == 0 or i == size - 1 or i == size // 2:
            print("x" * size)  
        else:
            print("x" + " " * (size - 2) + "x") 
    print()
