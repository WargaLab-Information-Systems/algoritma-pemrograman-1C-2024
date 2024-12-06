
n = int(input("Masukkan bilangan desimal: "))
if n <= 0:
    biner = "0"
else:
    biner = ""
    while n > 0:
        biner = str(n % 2) + biner
        n //=  2

print(f"Biner: {biner}")

for i in range(len(biner)):
    for j in range(i + 1):
        print(biner[j], end=' ')
    print()