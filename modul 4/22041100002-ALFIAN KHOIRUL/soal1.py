N = int(input("Masukkan ukuran sisi belah ketupat: "))
karakter1 = "x"


i = 0
while i < N:
    print(" " * (N - i - 1),end="" )
    
    j = 0
    while j < (2 * i + 1):
        if (i + j) % 2 == 0:
            print(karakter1, end="")
        else:
            print(karakter2, end="")
        j += 1
    print()
    i += 1

i = N 
while i >= 0:
    print(" " * (N - i - 1), end="")
    
    j = 0
    while j < (2 * i + 1):
        if (i + j) % 2 == 0:
            print(karakter1, end="")
        else:
            print(karakter2, end="")
        j += 1
    print()
    i -= 1