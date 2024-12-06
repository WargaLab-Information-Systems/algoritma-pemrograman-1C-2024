def cek_palindrom(kata):
    return kata == kata[::-1]
print (f"")

kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print(f"{kata} adalah palindrom.")
else:
    print(f"{kata} bukan palindrom.")