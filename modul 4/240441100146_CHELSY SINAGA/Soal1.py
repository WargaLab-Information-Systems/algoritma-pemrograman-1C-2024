while (True):
        n = int(input("Masukkan ukuran sisi belah ketupat: "))
        karakter= input("masukkan karakter (x atau o):")

        if karakter == "x" or karakter == "o":
                for i in range(n):
                 print(' ' * (n - i - 1) + (karakter + ' ') * (i + 1))
                for j in range(n -2, -1, -1):
                 print(' ' * (n - j - 1) + (karakter + ' ') * (j + 1))
                break
        else:
         print("input salah")
