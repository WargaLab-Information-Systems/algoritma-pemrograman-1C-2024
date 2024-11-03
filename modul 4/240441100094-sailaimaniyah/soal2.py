# Menerima input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi bilangan desimal ke biner
biner = ''
if desimal == 0:
    biner = '0'
else:
    while desimal > 0:
        biner = str(desimal%2) + biner
        desimal = desimal // 2

# membentuk pola segitiga
    i = 1
    for digit in biner:
        print(biner[:i])  # Menampilkan i digit pertama
        i += 1