desimal = int(input("Masukkan bilangan desimal: "))
asal_desimal = desimal  

biner = ""
while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + biner
    desimal = desimal // 2

max_digit = 0
temp_desimal = asal_desimal
while temp_desimal > 0:
    max_digit += 1
    temp_desimal //= 2

# segitiga
count = 0
for digit in biner:
    count += 1
    print(" " * (max_digit - count), end="")
    for i in range(count):
        print(biner[i], end="")
    print()