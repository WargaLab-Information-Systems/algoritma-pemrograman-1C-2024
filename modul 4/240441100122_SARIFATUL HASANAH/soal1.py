while True :
    sisi_N = int(input("Masukkan ukuran sisi belah ketupat : "))
    karakter = input("Masukkan karakter yang ingin digunakan ('X' atau 'O') : ")

    if karakter == "X" and "O" :
        for i in range(1, sisi_N + 1, 1):
            print(' ' * (sisi_N - i), end='')  
            for j in range(1, 2 * i):
                print(karakter, end='')  
            print()

        for i in range(sisi_N - 1, 0, -1):
            print(' ' * (sisi_N - i), end='')  
            for j in range(1, 2 * i):
                print(karakter, end='')  
            print()
        break
    else :
        print("Masukkan Huruf X atau O saja")

