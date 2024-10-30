tahun = int(input("Masukkan tahun: "))

# Memeriksa tahun kabisat
if tahun % 400 == 0:# % untuk mendapatkan sisa dari pembagian antara dua bilangan
    print(f"{tahun} adalah tahun kabisat.")
elif tahun % 100 == 0:
    print(f"{tahun} bukan tahun kabisat.")
elif tahun % 4 == 0:
    print(f"{tahun} adalah tahun kabisat.")
