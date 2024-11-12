while (True) :
    N = int(input("Masukkan tinggi belah ketupat: "))
    karakter = input("pola 'x' atau 'o' :")

    if karakter == 'x' or karakter == 'o':    
        # Bagian atas belah ketupat
        for i in range(N):
            print(" " * (N - i - 1), end="")
            print(karakter * (2 * i + 1))

        # Bagian bawah belah ketupat 
        for i in range(1, N):
            print(" " * i, end="")
            print(karakter * (2 * (N - i) - 1))
        break
    else:
        print("Error: karakter harus 'x' atau 'o'!")