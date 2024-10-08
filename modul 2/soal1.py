# menentukan nilai rata rata

# beri inputan nama dan nim 
nama = input ("Masukkan Nama Anda :")
NIM = input ("Masukkan NIM Anda :")

# beri inputan nilai yang akan dihitung dan di kategorikan
UTS = int (input("Masukkan Nilai UTS :"))
UAS = int (input("Masukkan Nilai UAS :"))

# beri rumus perhitungan rata rata
rata_rata= (UTS + UAS) / 2
print (rata_rata)


# hitung kategori nilai

nilai = (int(rata_rata))
if nilai >=  81 and nilai <= 100:
    print ("A")
elif nilai >= 71 and nilai <=80:
    print ("B")
elif nilai >=61 and nilai <=70:
    print ("C")
elif nilai >=41 and nilai <=60:
    print ("D")
elif nilai >=0 and nilai <=40:
    print ("E")  