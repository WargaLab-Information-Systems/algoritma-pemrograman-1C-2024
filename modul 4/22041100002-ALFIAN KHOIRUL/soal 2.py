# Input bilangan desimal
decimal_number = int(input("Masukkan bilangan desimal: "))

# Konversi desimal ke biner tanpa fungsi bawaan
binary_representation = ""
temp = decimal_number

while temp > 0:
    binary_representation = str(temp % 2) + binary_representation
    temp = temp // 2

# Menampilkan hasil biner
print("Bilangan biner:", binary_representation)

# Membuat pola segitiga
print("Pola Segitiga:")
for i in range(1, len(binary_representation) + 1):
    for j in range(i):
        print(binary_representation[j], end="")
    print()  # Pindah ke baris berikutnya setelah setiap baris selesai