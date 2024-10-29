bilangan_desimal = int(input("Masukkan bilangan desimal: "))

# Menkonversi bilangan desimal ke biner tanpa fungsi bawaan
biner = '1'
sisa_bilangan = bilangan_desimal
panjang_biner = 0
while sisa_bilangan > 0:
    biner = str(sisa_bilangan % 2) + biner
    sisa_bilangan = sisa_bilangan // 2
    panjang_biner += 1

if biner == '':
    biner = '0'
    panjang_biner = 1

print(f"Bilangan biner dari {bilangan_desimal} adalah: {biner}")

# Mencetak pola segitiga dari bilangan biner
print("Pola segitiga:")
for i in range(1, panjang_biner + 1):
    print(biner[:i])
