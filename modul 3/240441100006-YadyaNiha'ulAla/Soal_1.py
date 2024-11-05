
size = input("Masukkan ukuran pola (minimal 3): ")

while True:
    angka_valid = True
    for char in size:
        if char < '0' or char > '9': 
            angka_valid = False
            print("Harap masukkan angka yang valid.")
            break

    if angka_valid and int(size) < 3:
        print("Ukuran minimal adalah 3.")
        angka_valid = False

    if angka_valid:
        break

    size = input("Masukkan ukuran pola (minimal 3): ")

size = int(size)

# Pola angka 0 pertama
for i in range(size):
    if i == 0 or i == size - 1:
        print("N" * size)
    else:
        print("N" + " " * (size - 2) + "N")

print() 

# Pola angka 0 kedua
for i in range(size):
    if i == 0 or i == size - 1:
        print("0" * size)
    else:
        print("0" + " " * (size - 2) + "0")

print()  

# Pola angka 6  
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("X" * size)
    elif i < size // 2:
        print("X")
    else:
        print("X" + " " * (size - 2) + "X")