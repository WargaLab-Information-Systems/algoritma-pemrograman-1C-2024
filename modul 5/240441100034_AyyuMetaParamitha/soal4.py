def cek_palindrom(kata):
    # Menghilangkan spasi dan mengubah semua huruf menjadi kecil
    kata = kata.replace(" ", "")

    
    return kata == kata[::-1]

while True:
    katainput = input("Masukkan kata untuk dicek: ")
    
    # Cek apakah kata adalah palindrom
    if cek_palindrom(katainput):
        print(f"{katainput} adalah palindrom.")
    else:
        print(f"{katainput} bukan palindrom.")

    break