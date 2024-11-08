desimal = int(input("Masukkan bilangan desimal: "))
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
print("Dan pola segitiganya:")
for c in range (1, panjang + 1):
    print(biner[:c])