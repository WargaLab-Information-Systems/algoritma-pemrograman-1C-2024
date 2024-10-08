nama= input("masukkan nama ")
skor= int(input("masukkan skor: "))
ipk= float(input("masukkan IPK: "))

print("Nama anda",nama)
if skor>1100 and ipk>3.0:
    print("lulus persyaratan")
else:
    print("tidak lulus persyaratan")