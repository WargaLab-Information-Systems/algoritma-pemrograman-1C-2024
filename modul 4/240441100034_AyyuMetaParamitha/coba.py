desimal = int(input("Masukkan bilangan desimal: "))

# desimal ke biner secara manual
biner = ''
if desimal == 0:
    biner = '0'
else:
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal //= 2

# Mencetak pola segitiga
jumlah_karakter = 0
for karakter in biner:
    jumlah_karakter += 1

# Menggunakan loop untuk mencetak karakter satu per satu
for i in range(1, jumlah_karakter + 1):
    for j in range(i):  # Mencetak i karakter
        print(biner[j], end='')  # Cetak karakter biner tanpa newline
    print()  # Pindah ke baris baru setelah mencetak satu baris

  