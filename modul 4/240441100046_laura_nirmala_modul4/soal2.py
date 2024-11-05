# Mengambil input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Validasi input negatif
if desimal < 0:
    print("Masukkan bilangan desimal non-negatif.")
else:
    # Konversi desimal ke biner secara manual
    biner = ''
    if desimal == 0:
        biner = '0'
    else:
        while desimal > 0:
            biner = str(desimal % 2) + biner
            desimal //= 2 # // pembagian integer (7//2=3)

    # Menampilkan pola segitiga
    i = 1
    for digit in biner:
        print(biner[:i])  # Menampilkan i digit pertama i untuk mencetak bagian bertahap dari string biner
        i += 1 #menambahkan nilai variabel dalam loop
