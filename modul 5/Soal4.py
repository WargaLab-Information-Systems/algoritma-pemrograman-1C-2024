def cek_palindrom(kata):
    # membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

kata = input("Masukkan kata: ")
if cek_palindrom(kata):
    print(f"{kata} adalah palindrom")
else:
    print(f"{kata} bukan palindrom")
    print(f"{kata[::-1]}")
    

