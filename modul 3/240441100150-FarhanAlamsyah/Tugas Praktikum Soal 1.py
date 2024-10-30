size = int(input("Masukkan panjang dan lebarnya: "))  # Anda bisa mengubah ukuran sesuai kebutuhan

for i in range(size):
    if i == 0:
        print(" " * (size // 2) + "1")
    elif i == size - 1:
        print(" " * (size // 2) + "1")
    else:
        print(" " * (size // 2) + "1")
print(" ")

for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("5" * size)
    elif i < size // 2:
        print("5" + " " * (size - 2) + " ")
    else:
        print(" " * (size - 1) + "5")
print(" ")

for i in range(size):
    if i == 0 or i == size - 1:
        print("0" * size)
    elif i < size - 1:
        print("0" + " " * (size - 2) + "0")
print(" ")