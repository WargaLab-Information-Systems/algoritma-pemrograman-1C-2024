inputan = int(input("Masukkan angka: "))
for i in range(2):
     # Membuat pola angka 0
    for i in range(5):
        for j in range(5):
            if i == 0 or i == (inputan-1) or j == 0 or j == (inputan-1):
                print("*", end=" ")
            else:
                print("*", end=" ")
        print()
    print("")

# Membuat pola angka 2
for i in range(5):
    for j in range(5):
        if i == 0 or i == 2 or i == 4:
            print("*", end=" ")
        elif i == 1 and j == 4:
            print("*", end=" ")
        elif i == 3 and j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()