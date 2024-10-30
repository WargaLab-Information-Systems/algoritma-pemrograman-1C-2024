# Input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi desimal ke biner
biner = ''
while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal //= 2
print(f"hasil biner: {biner}")
# Mencetak pola segitiga dari bilangan biner
for i in range(1, len(biner) + 1):
    print(biner[:i])
