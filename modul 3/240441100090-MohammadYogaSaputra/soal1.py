ukuran = int(input("Masukan Ukuran : "))

for i in range(ukuran):
    if i == 0 or i == ukuran - 1:
        print("0" * ukuran)
    else:
        print("0" + " " * (ukuran - 2) + "0")
print() 

for i in range(ukuran):
    if i == 0 or i == ukuran // 2 or i == ukuran - 1:
        print("x" * ukuran)
    elif i < ukuran // 2:
        print("y" + " " * (ukuran - 2) + "y")
    else:
        print(" " * (ukuran - 1) + "y")
print()  

for i in range(ukuran):
    if i == 0 or i == ukuran - 1:
        print("0" * ukuran)
    else:
        print("0" + " " * (ukuran - 2) + "0")

