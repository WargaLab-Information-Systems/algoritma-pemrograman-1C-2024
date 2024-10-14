# Program utama dalam loop
while True:
    # Meminta input NIM dari pengguna
    nim_terakhir = input("Masukkan NIM terakhir (misal NIM ARZHA ITU 062): ")

    # Mencetak digit satu per satu secara menurun agar terbentuknya angka atau NIM  yang diinginkan
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

   
    ulang = input("Apakah Anda ingin mengulang? (ya/tidak): ")

    
    if ulang != 'ya' and ulang != 'Ya':
        break

print("Program selesai.")

# soal 1