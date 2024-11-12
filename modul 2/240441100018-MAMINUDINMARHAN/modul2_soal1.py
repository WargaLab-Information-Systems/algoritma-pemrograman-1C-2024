nama = str(input("Masukkan Nama "))
NIM = str(input("Masukkan NIM "))
UTS = float(input("Masukkan Nilai UTS "))
UAS = float(input("Masukkan Nilai UAS "))
rata_rata = (UTS + UAS) / 2
print(f"Masukkan Nama {nama}")
print(f"NIM anda {NIM}")
print(f"Nilai rata rata nilai anda {rata_rata}")
if rata_rata <= 100 and rata_rata >= 81:
    print("Anda Mendapatkan Nilai A")
elif rata_rata <= 80 and rata_rata >= 71:
    print("Anda Mendapatkan Nilai B")
elif rata_rata <= 70 and rata_rata >= 61:
    print("Anda Mendapatkan Nilai C")
elif rata_rata <= 60 and rata_rata >= 41:
    print("Anda Mendapatkan Nilai D")
else:
    if rata_rata <= 40 and rata_rata >= 0:
        print("Anda Mendapatkan Nilai E")