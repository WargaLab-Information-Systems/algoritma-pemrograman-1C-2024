karakter = input("Masukkan karakter untuk pola (misalnya 'X' atau 'O'): ")
size = int(input("Masukkan ukuran belah ketupat (N): "))

for i in range (size):
    for j in range (size,i,-1):
        print(' ',end=' ')
    for j in range (2*i+1):
        print(karakter,end=' ')
    print()
for i in range (size-2,-1,-1):
    for j in range (size,i,-1):
        print(' ',end=' ')
    for j in range (2*i+1):
        print(karakter,end=' ')
    print()