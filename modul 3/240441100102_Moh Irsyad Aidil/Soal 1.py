tinggi = int(input("Masukkan tinggi angka : "))

# membuat pola angka dengan menggunakan x pola angka 1
for kolom in range (tinggi):
    print(" " * (tinggi) + "x")
print() 


# mambuat pola angka dengan menggunakan x pola angka "0"

for kolom in range(tinggi):
    for baris  in range(tinggi):
        if   kolom  == 0 or kolom  == tinggi - 1  or baris  == 0 or baris == tinggi - 1 :
            print("X", end="")
        else:
            print(" ", end="")
    print()
print()

#mambuat pola angka dengan menggunakan x pola angka "2"
for baris in range(tinggi):
    for kolom in range(tinggi):
        if baris == 0 or baris == tinggi // 2 or baris == tinggi - 1 :
            print("x", end="")
        elif baris < tinggi // 2 and kolom == tinggi - 1:
            print("x", end="")
        elif baris > tinggi // 2 and kolom == 0:
            print("x", end="")
        else:
            print(" ", end="")
    print()
  



















































