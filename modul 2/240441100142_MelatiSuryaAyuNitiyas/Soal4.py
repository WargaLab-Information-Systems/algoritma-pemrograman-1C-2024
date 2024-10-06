# input tahun 
tahun = int(input("Masukkan tahun yang ingin dicek: "))

# apakah tahun tersebut kabisat atau bukan
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
