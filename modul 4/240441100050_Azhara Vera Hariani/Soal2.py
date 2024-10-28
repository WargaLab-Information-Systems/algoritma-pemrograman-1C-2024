# Mengambil input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Konversi desimal ke biner secara manual
biner = ''   # tempat buat menyimpan bilangan biner yang sudah dikonfersi bilangan desimal 
if desimal == 0: #jika kita menginputkan 0 maka binernya muncul 0
    biner = '0'
else:
    while desimal > 0: #jika kita menginputkan lebih dari 0 maka akan memproses menggunakan rumus tersebut
        biner = str(desimal % 2) + biner
        desimal //= 2

# Menampilkan pola segitiga
i = 1
while True:
    if i <= 0:
        break

    angka = biner[i - 1:i]
    if angka == '':
        break

    print (biner[:i])  # akan mencetak bertahap bagian dari string biner
    i += 1       # digunakan untuk menambah nilai variabel dalam loop, membantu dalam mengontrol jumlah iterasi
