# while
#  contoh 1
# x = "wulan"
# while x :
#     print (x)
#     x = x[1 :]

#contoh 2
# a = 0
# b = 10
# while a < b :
#     print (a)
#     a = a + 1

#For
#coba

# for a in range (1,5):
#     print(a)

#  a = 1
# while True :
#     if a >= 5:
#         break
#     print(a)
#     a += 1

# a = 1
# while a < 5:
#     print (a)
#     a += 1

#contoh break
# x = 4
# while x < 5 :
#     if x == 3 :
#         break
#     print(x)
#     x = x + 1

# else :
#     print("Loop sudah selesai dikerjakan")

#contoh continue
# n = 10
# while n:
#     n = n - 1
#     if n % 2 != 0:
#         continue
#     print (n)

#contoh Pass
# while True :
#     pass
# Loop untuk baris bagian atas hingga tengah
for i in range(N): # type: ignore
    # Cetak spasi di depan karakter untuk membuat bentuk belah ketupat
    print(' ' * (N - i - 1), end='')

    # Cetak karakter yang dipilih
    for j in range(2 * i + 1):
        print(karakter, end='') # type: ignore
    print()  # Pindah ke baris berikutnya

# Loop untuk baris bagian tengah ke bawah
for i in range(N - 2, -1, -1):
    # Cetak spasi di depan karakter untuk membuat bentuk belah ketupat
    print(' ' * (N - i - 1), end='')

    # Cetak karakter yang dipilih
    for j in range(2 * i + 1):
        print(karakter, end='') # type: ignore
    print()  # Pindah ke baris berikutnya