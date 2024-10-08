tahun = int(input("Masukkan tahun:"))
if(tahun % 4 == 0):
    print("Tahun kabisat")
elif(tahun % 100 == 0):
    print("Bukan tahun kabisat")
elif(tahun % 400 == 0):
    print("Tahun kabisat")
else :
    print("Bukan tahun kabisat")


# Tahun kabisat merupakan tahun yang habis dibag 4
# Jika bisa habis dibagi 100 maka harus habis dibagi 400
