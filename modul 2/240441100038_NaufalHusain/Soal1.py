# program menentukan nilai rata rata

# masukan inputan nama dan nim secara dinamis
Nama = input("Masukan Nama : ")
Nim = input("Masukan Nim : ")

# masukkan inputan nilai yang akan dihitung 
UTS = int(input("Masukkan Nilai UTS : "))
UAS = int(input("Masukkan Nilai UAS : "))

# Menghitung rata-rata
rata_rata = (UTS + UAS)/2
print(f"Nilai rata rata Anda : {float(rata_rata)} ")


# Menentukan nilai huruf

nilai = (int(rata_rata))
if nilai <= 100 and nilai >= 81:
   kategori = "A"
elif nilai <= 80 and nilai >=71:
    kategori = "B"
elif nilai <= 70 and nilai >= 61:
    kategori = "C"
elif nilai <= 60 and nilai >= 41:
    kategori = "D"
elif nilai <= 40 and nilai > 31:
    kategori = "E"
elif nilai <= 30 and nilai >= 0:
    kategori = "F"
else:
    kategori = ("Nilai Anda Tidak Valid")

print(f"Anda Mendapatkan Nilai : {kategori} ")




