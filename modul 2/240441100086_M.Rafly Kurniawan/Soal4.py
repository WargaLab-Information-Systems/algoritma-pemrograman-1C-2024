tahun = int(input("Masukkan tahun yang ingin dicek :"))
if(tahun % 4 == 0, tahun %100 !=0) or (tahun %400 == 0) :
    print(tahun, "adalah tahun kabisat")
else :
    print(tahun, "bukan tahun kabisat")