#input ukuran
size = int(input("Masukkan Size: "))

# angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print("n" * size)
    else:
        print("x" + " " * (size - 2) + "x")

print()

# angka 8
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("h" * size)
    else:
        print("x" + " " * (size - 2) + "n")

print()

# Pola angka 6
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("1" * size)
    elif i < size // 2:
        print("x")
    else:
        print("x" + " " * (size - 2) + "x")
