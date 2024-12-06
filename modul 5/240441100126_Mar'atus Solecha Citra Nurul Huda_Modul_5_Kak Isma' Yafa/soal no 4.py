def cek_palindrom(kata) :
    return kata == kata [::-1]

kata = input("masukkan kata : ")
if cek_palindrom(kata) :
    print(f"{kata} adalah polindrom")
else :
    print(f"{kata} bukan polindrom")