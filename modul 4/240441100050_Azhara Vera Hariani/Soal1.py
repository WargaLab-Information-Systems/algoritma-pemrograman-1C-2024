N = int(input("Masukkan ukuran sisi checkerboard yang diinginkan: "))
karakter = input("pilihlah karakter :(X/O)")

# Pola untuk membangun bagian atas belah ketupat
for i in range(0,N+1):  # setiap kebawah +1
    for j in range(0,N-i):
        print(end=" ")   # Menggabungkan Output dalam satu baris
    for j in range(0,i):
        print(karakter,end=" ")
    print()

# Pola untuk membangun bagian bawah belah ketupat
if i==N:
    for i in range(N-1,0,-1):  # semakin kebawah -1
        for j in range(0,N-i):
            print(end=" ")
        for j in range(0,i):
            print(karakter,end=" ")
        print()