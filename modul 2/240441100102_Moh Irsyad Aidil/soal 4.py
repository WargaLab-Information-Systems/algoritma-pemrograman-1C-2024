tahun = int(input("masukan tahun :"))
if tahun % 4 == 0 and tahun % 400== 0:
    print (f"tahun {tahun} merupakan tahun kabisat")
elif (tahun % 100 == 0):
    print (f"tahun {tahun}bukan tahun kabisat")
else :
    print(f"tahun {tahun} bukan tahun kabisat")