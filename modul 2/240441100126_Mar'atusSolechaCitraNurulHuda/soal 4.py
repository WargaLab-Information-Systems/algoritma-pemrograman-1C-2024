# Program untuk menentukan tahun kabisat

# # Fungsi untuk mengecek tahun kabisat
#  if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     return True
# else:
#     return False


# # Input tahun dari pengguna
# try:
#     tahun = int(input("Masukkan tahun: "))
#     if is_kabisat(tahun):
#         print(f"{tahun} adalah tahun kabisat.")
#     else:
#         print(f"{tahun} bukan tahun kabisat.")
# except ValueError:
#     print("Silakan masukkan angka yang valid.")

# tahun = int(input("Masukkan tahun: "))

# if (tahun % 4) == 0:
#     if (tahun % 100) == 0:
#         if (tahun % 400) == 0:
#             print(tahun, "merupakan tahun kabisat.")
#         else:
#             print(tahun, "bukan tahun kabisat.")
#     else:
#         print(tahun, "merupakan tahun kabisat.")
# else:
#     print(tahun, "bukan tahun kabisat.")

# INPUT TAHUN
tahun = int(input("masukkan tahun yang akan kamu cek : "))

# RUMUS MENENTUKAN APAKAH TAHUN TERSEBUT MERUPAKAN TAHUN KABISAT ATAU BUKAN
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} merupakan tahun kabisat.")
else :
    print(f"{tahun} bukan termasuk dalam tahun kabisat.")