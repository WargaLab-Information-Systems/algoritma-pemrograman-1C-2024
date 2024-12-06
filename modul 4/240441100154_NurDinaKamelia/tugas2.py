n= int(input("Masukkan bilangan desimal:"))
biner = ""
konvers = n
while n > 0:
    biner = str(n%2) + biner
    n = n//2
print("Hasil konversi bilangan desimal", konvers, "ke biner adalah", biner)
print(f"pola segitiga:")
for i in range(1, len(biner) + 1):
    print(biner[:i])



