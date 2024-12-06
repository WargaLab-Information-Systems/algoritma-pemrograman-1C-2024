def cek_palindrom(kata):
    kata = kata.lower()
    panjang = len(kata)
    for i in range(panjang // 2):
        if kata[i] != kata[panjang - i - 1]:
            return False
    return True

kata = input("Masukkan kata: ")
print(f"{kata} adalah palindrom." if cek_palindrom(kata) else f"{kata} bukan palindrom.")
