angka = int(input("Masukkan bilangan desimal: "))
biner = ''

while angka > 0:
    biner = str(angka % 2) + biner
    angka //= 2
print(biner)
for i in range(1, len(biner) + 1):
    print(biner[:i])
