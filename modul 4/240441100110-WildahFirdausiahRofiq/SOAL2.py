# Meminta input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Proses konversi desimal ke biner
biner = ""
while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + biner  # Menambahkan sisa ke depan string biner
    desimal = desimal // 2

# Menampilkan hasil konversi biner
print(f"Bilangan biner: {biner}")

# Menampilkan pola segitiga
print("\nPola Segitiga:")
for i in range(1, len(biner) + 1):
    print(biner[:i])  # Menampilkan i digit pertama dari biner