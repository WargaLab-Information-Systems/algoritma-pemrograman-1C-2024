# menentukan tahun kabisat

tahun = int(input("masukkan tahunnya : "))
if tahun % 4 == 0 and tahun % 400 == 0:
    print(f"tahun {tahun} merupakan tahun kabisat")
elif tahun % 100 == 0:
    print(f"tahun {tahun} bukan tahun kabisat")
else :
    print(f"{tahun} bukan tahun kabisat!!!")
