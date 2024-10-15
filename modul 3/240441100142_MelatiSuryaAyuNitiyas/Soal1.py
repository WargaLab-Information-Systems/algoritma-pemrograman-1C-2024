tinggi = int(input("Masukkan tinggi: "))

# 1
for baris in range(tinggi):
    print("  x")

print()
print("\n")  

# 4
for baris in range(tinggi):
    for kolom in range(tinggi):
        if kolom == tinggi - 1:
            print("x", end="")
        elif baris == tinggi // 2:
            print("x", end="")
        elif baris < tinggi // 2 and kolom == 0:
            print("x", end="")
        else:
            print(" ", end="")
    print()
print("\n")

# 2
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
print("\n")