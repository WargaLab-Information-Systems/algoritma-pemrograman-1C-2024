bilangan_desimal = int(input("Masukkan bilangan desimal: "))
biner = ""

#desimal ke biner
while bilangan_desimal > 0:
  sisa = bilangan_desimal % 2
  biner = str(sisa) + biner
  bilangan_desimal //= 2

#cetak dalam bentuk segitiga
for i in range(len(biner)): #untuk mendapatkan jumlah karakter dalam string biner
  print(biner[:i+1]) #untuk mengambil potongan dari string biner



