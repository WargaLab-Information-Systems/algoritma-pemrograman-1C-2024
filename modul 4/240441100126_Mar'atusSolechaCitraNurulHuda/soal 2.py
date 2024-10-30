# Input bilangan desimal
desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi bilangan desimal ke biner tanpa menggunakan fungsi bin()
biner = ""
if desimal == 0 :
    biner = '0'
else :
    while desimal > 0:
        biner = biner + str(desimal % 2)   # Mendapatkan sisa pembagian 2 dan menambahkannya ke depan string biner
        desimal = desimal // 2            # Memperbarui desimal dengan hasil bagi 2

# Menampilkan pola segitiga
for i in range(1, len(biner) + 1):
    print(biner[:i])  # Mencetak i digit pertama dari bilangan biner
