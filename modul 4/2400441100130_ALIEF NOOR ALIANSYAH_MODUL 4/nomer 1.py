ukuran = int(input("masukkan ukuran : "))
karakter = input("masukkan karakter (X/O) : ").upper()

if karakter in {"X", "O"}:
    for i in range(1, ukuran + 1):
        for j in range (ukuran - i):
            print('H', end=" ")
        for k in range (1, i + 1):
            print(karakter, end="   ")
        print()

    for i in range(1, ukuran +1):
        for j in range (1, i +1):
            print(' ',end=" ")
        for k in range (ukuran - i):
            print(karakter, end="   ")
        print()

else :
    print("Input tidak valid, Harap masukkan karakter 'X' ATAU 'O' ")