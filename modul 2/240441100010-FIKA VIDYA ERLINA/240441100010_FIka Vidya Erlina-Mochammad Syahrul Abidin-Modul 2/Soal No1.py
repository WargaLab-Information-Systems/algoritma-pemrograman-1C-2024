nama= input("masukkan nama: ")
nim= input("masukkan nim: ")
Nilai_UTS=int(input("masukkan nilai uts: "))
Nilai_UAS= int(input("masukkan nilai uas: "))

Nilai_rata_rata= (Nilai_UTS + Nilai_UAS)/2

if 81 <= Nilai_rata_rata <= 100:
    nilai='A'
elif 71 <= Nilai_rata_rata <= 80:
    nilai= 'B'
elif 61 <= Nilai_rata_rata <= 70:
    nilai= 'C'
elif 41 <= Nilai_rata_rata <= 60:
    nilai= 'D'
elif 0 <= Nilai_rata_rata <= 40:
    nilai= 'E'
else: 
    nilai= 'nilai tidak valid'
    
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Nilai rata rata: {Nilai_rata_rata}")
print(f"Anda mendapatkan nilai: {nilai}")
