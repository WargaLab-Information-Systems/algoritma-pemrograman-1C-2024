desimal = int(input("Masukkan bilangan desimal: "))
biner = ''
while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal //= 2
print("Bilangan biner:", biner)
print("Pola segitiga:")
for i in range(1, len(biner) + 1):
    print(biner[:i])