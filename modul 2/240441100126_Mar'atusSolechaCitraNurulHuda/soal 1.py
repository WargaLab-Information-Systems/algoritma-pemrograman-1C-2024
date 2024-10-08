# nama = "Wuland"
# nim = 150451100006
# nilai_uts = 100
# nilai_uas = 90 


nama = input("masukkan nama: ")
nim = int(input("masukkan nim: "))
nilai_UTS = int(input("masukkan nilai UTS: "))
nilai_UAS = int(input("masukkan nilai UAS: "))
print("masukkan nama : ", nama)
print("masukkan nim : ", nim)
# Menghitung rata-rata
rata_rata = int(nilai_UTS + nilai_UAS)/ 2
# Menampilkan hasil
print("Nilai rata-rata kamu:", rata_rata)
if rata_rata <= 100 and rata_rata >= 81 : 
     print("kamu mendapat nilai A")
elif rata_rata <= 100 and rata_rata >= 71:
    print("kamu mendapat nilai B")
elif rata_rata <= 100 and rata_rata >= 61:
    print("kamu mendapat nilai C")
elif rata_rata <= 100 and rata_rata >= 41:
    print("kamu mendapat nilai D")
elif rata_rata <= 100 and rata_rata >= 0 :
    print("kamu mendapat nilai E")
else : 
    print("nilai tidak valid")