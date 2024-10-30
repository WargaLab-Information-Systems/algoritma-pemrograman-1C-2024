desimal = int(input("Masukkan bilangan desimal: "))
if desimal == 0:
    biner = "0"
else:
    biner = ""
    n = desimal
    while n > 0:              #untuk mengkonversi desimal ke biner
        biner = str(n % 2) + biner
        n //= 2

print(f"Biner: {biner}")

for i in range(len(biner)):   #len untuk mentahui panjang string yaitu digit biner
    for j in range(i + 1):    #i mengontrol baris 0,j mengontrol kolom 0 sampai i + 1
        print(biner[j], end=' ') 
    print()  