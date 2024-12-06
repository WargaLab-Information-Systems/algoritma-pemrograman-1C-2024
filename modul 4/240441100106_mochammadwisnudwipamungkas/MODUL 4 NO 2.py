angka = int(input("Masukkan bilangan desimal: "))
hasil = ""
while angka > 0: #jumlah perulangan belum di ketahui
    hasil = str(angka % 2) + hasil #modulus =biner
    angka //= 2 
for i in range(1, len(hasil) + 1): #menghitung jumlah nilai dalam bentuk str yang sudah di ketahui
    print(hasil[:i])