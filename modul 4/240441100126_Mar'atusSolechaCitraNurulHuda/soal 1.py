n = int(input("Masukkan ukuran sisi belah ketupat (n): ")) # panjang sisi
karakter = input("Masukkan karakter ('X' atau 'O'): ")
if karakter == "x" and "o" :
  
    for i in range(1, n + 1):
        for j in range (n - i):
            print(' ', end=" ")
        for k in range (1, i + 1):
            print(karakter, end="   ")
        print()

    for i in range(1, n + 1):
        for k in range (1, i + 1):
            print(' ',end=" ")
        for J in range (n - i):
            print(karakter, end="   ")
        print()

else :
    print("karakter tidak sesuai")