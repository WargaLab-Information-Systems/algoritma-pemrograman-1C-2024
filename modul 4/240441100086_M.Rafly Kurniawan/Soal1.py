n = int(input("Masukkan Ukuran : "))
karakter = input("Masukkan karakter antara (X / O) : ").upper()

if karakter == "X" or karakter == "O":
    for i in range(n): 
        # Spasi
        for j in range(n - i - 1):
            print(" ", end="")
        # Karakter
        for j in range(i + 1):
            print(karakter + " ", end="")
        print() 

    for i in range(n - 1):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(n - i - 1):
            print(karakter + " ", end="")
        print()
else:
    print("Karakter tidak valid. Silakan masukkan 'X' atau 'O'.")