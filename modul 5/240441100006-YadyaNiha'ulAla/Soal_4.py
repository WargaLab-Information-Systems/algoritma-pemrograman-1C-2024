def cek_palindrom(kata):
    panjang = len(kata)
    for i in range(panjang // 2):
        if kata[i] != kata[panjang - i - 1]:
            return False
    return True

print("--- Cek Palindrom ---")

kata = input("Masukkan sebuah kata: ")
print(cek_palindrom(kata))