# input bilangan desimal dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# ubah bilangan desimal ke biner secara manual
if desimal == 0:
    biner = "0"
else :
    biner = ""
while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + biner
    desimal = desimal // 2
panjang = 0
for i in biner:
    panjang += 1
print(f"Bentuk biner dari {desimal} adalah {biner}")
print("Dan pola segitiganya: ")
# cetak pola segitiga dari bilangan biner
for i in range(1, panjang + 1):
    print(biner[:i])