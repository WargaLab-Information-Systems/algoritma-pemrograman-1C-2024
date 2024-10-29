# Mengambil input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi desimal ke biner
biner = ""
while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal = desimal // 2

# Menampilkan hasil dalam bentuk pola segitiga
for i in range(1, len(biner) + 1):
    print(biner[:i])
