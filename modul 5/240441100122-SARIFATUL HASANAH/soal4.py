def cek_palindrom(kata):
    kata = kata.replace(" ", "")
    return kata == kata[::-1]

kata = input("Masukkan kata yang ingin dicek: ").lower()

if cek_palindrom(kata):
    print(f"{kata} adalah palindrom.")
    print(f"{kata[::-1]}")
else:
    print(f"{kata} bukan palindrom.")
    print(f"{kata[::-1]}")


