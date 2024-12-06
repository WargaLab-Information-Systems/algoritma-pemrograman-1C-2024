tahun = int(input("Masukkan tahun: "))
if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print(f"Tahun {tahun} merupakan tahun kabisat")
        else:
            print(f"Tahun {tahun} bukan merupakan tahun kabisat")
    else:
        print(f"Tahun {tahun} merupakan tahun kabisat")
else:
    print(f"Tahun {tahun} bukan merupakan tahun kabisat")