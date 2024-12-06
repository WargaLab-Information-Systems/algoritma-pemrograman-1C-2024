karakter = str(input("masukkan bentuk (misal X/O) : ")).upper()
ukuran = int(input("masukkan ukuran : "))
if karakter in ("X", "O"):
    for a in range(1, ukuran +1):
        for b in range (ukuran - a):
            print(' ', end=" ")
        for c in range (1, a+ 1):
            print(karakter, end="   ")
        print()
    for a in range(1, ukuran +1):
        for b in range (1, a +1):
            print(' ',end=" ")
        for c in range (ukuran - a):
            print(karakter, end="   ")
        print()
else:
    print("Input tidak valid")