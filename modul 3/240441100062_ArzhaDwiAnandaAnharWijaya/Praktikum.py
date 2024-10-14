# # coba while

# x = "arzha" 
# while x :
#     print (x)
#     x= x[1 :]

# # contoh 2
# a = 0
# b = 15
# while a <= b : 
#     print (a)
#     a = a + 1

# contoh 3 (for)

# Program menggunakan for untuk mencetak NIM terakhir

# nim_terakhir = "062"

# for digit in nim_terakhir:
#     print(digit)


# x = 4
# while x < 100 :
#     if x == 89 :
#         break
#     print(x)
#     x = x+1
# else :
#     print ("loop sudah dikerjakan")

# # coba continue
# n = 10
# while n :
#     n = n-1
#     if n%2

# # Meminta input dari pengguna
# angka = input("Masukkan angka bulat: ")

# # Membalikkan urutan angka menggunakan while
# angka_balik = ""
# i = len(angka) - 1

# while i >= 0:
#     angka_balik += angka[i]  # Menambahkan digit di belakang
#     i -= 1

# # Menampilkan hasil
# print("Angka setelah dibalik: " + angka_balik)

# Program utama dalam loop
while True:
    # Meminta input NIM dari pengguna
    nim_terakhir = input("Masukkan NIM terakhir (misal NIM ARZHA ITU 062): ")

    # Mencetak digit satu per satu secara menurun
    for digit in nim_terakhir:
        if digit == '0':
            print(" xxx ")
            print("x   x")
            print("x   x")
            print("x   x")
            print(" xxx ")
        elif digit == '1':
            print("  x  ")
            print(" xx  ")
            print("  x  ")
            print("  x  ")
            print(" xxxx")
        elif digit == '2':
            print(" xxx ")
            print("    x")
            print(" xxx ")
            print("x    ")
            print(" xxx ")
        elif digit == '3':
            print(" xxx ")
            print("    x")
            print(" xxx ")
            print("    x")
            print(" xxx ")
        elif digit == '4':
            print("x   x")
            print("x   x")
            print(" xxxx")
            print("    x")
            print("    x")
        elif digit == '5':
            print(" xxx ")
            print("x    ")
            print(" xxx ")
            print("    x")
            print(" xxx ")
        elif digit == '6':
            print(" xxx ")
            print("x    ")
            print(" xxx ")
            print("x   x")
            print(" xxx ")
        elif digit == '7':
            print(" xxx ")
            print("    x")
            print("   x ")
            print("  x  ")
            print(" x   ")
        elif digit == '8':
            print(" xxx ")
            print("x   x")
            print(" xxx ")
            print("x   x")
            print(" xxx ")
        elif digit == '9':
            print(" xxx ")
            print("x   x")
            print(" xxx ")
            print("    x")
            print(" xxx ")

        print()  # Memisahkan setiap digit

    # Menanyakan apakah ingin mengulang program
    ulang = input("Apakah Anda ingin mengulang? (ya/tidak): ")

    # Jika tidak ingin mengulang, keluar dari loop
    if ulang != 'ya' and ulang != 'Ya':
        break

print("Program selesai.")
