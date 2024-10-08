tahun_input = int(input("masukkan tahun: "))
# Menentukan apakah tahun kabisat
if (tahun_input % 400 == 0):
    print(f"{tahun_input} adalah tahun kabisat.")
elif (tahun_input % 4 == 0):
    print(f"{tahun_input} adalah tahun kabisat.")
elif (tahun_input % 100 != 0):
    print(f"{tahun_input} bukan tahun kabisat.")
else:
    print("Input tidak valid. Harap masukkan angka yang valid.")