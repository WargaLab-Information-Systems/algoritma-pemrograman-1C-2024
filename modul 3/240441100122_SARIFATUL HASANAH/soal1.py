size = int(input("Masukkan size : "))
print()

#membuat angka 1
for kolom in range(size) :
    for baris in range(size) :
        if  baris == size // 2 :
            print("1",end=" ")
        else :
            print("",end=" ")
    print()
print("\n")

#membuat angka 2
for baris in range(size):
    for kolom in range(size):
        if baris == 0 or baris == size // 2 or baris == size - 1 :
            print("2", end="")
        elif baris < size // 2 and kolom == size - 1:
            print("x", end="")
        elif baris > size // 2 and kolom == 0:
            print("n", end="")
        else:
            print(" ", end="")
    print()  
print("\n")

#membuat angka 2
for baris in range(size):
    for kolom in range(size):
        if baris == 0 or baris == size // 2 or baris == size - 1 :
            print("2", end="")
        elif baris < size // 2 and kolom == size - 1:
            print("x", end="")
        elif baris > size // 2 and kolom == 0:
            print("h", end="")
        else:
            print(" ", end="")
    print()  
