# program mengonversi bilangan desimal ke biner dalam bentuk segitiga
desimal = int(input("Masukkan Bilangan Desimal : "))
if desimal == 0:
    biner = "0"
else:
    biner = ""
    a = desimal
    while a > 0:
        sisa = a % 2
        biner = str(sisa) + biner
        a //= 2

panjang = 0
for b in biner:
    panjang += 1
print(f"Bentuk biner dari {desimal} adalah {biner}")
print("Berikut bentuk pola segi tiganya :")
for i in range (1, panjang + 1):
    print(biner[:i])