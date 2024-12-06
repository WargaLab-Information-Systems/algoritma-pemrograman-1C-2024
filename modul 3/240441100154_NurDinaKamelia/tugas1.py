# # # Fungsi untuk mencetak angka 1
# # def print_number_1(size):
# #     for row in range(size):
# #         if row == 0:
# #             print(' ' * (size - 1) + '*')
# #         else:
# #             print(' ' * (size - 2) + '**')

# # # Fungsi untuk mencetak angka 5
# # def print_number_5(size):
# #     for row in range(size):
# #         if row == 0 or row == size // 2 or row == size - 1:
# #             print('*' * size)
# #         elif row < size // 2:
# #             print('*')
# #         else:
# #             print('*' + ' ' * (size - 2) + '*')

# # # Fungsi untuk mencetak angka 4
# # def print_number_4(size):
# #     for row in range(size):
# #         if row == size // 2:
# #             print('*' * size)
# #         elif row < size // 2:
# #             print('*' + ' ' * (size - 2) + '*')
# #         else:
# #             print(' ' * (size - 1) + '*')

# # # Fungsi utama untuk mencetak angka 154
# # def print_number_154(size):
# #     for row in range(size):
# #         # Cetak angka 1
# #         if row == 0:
# #             print_number_1(size)
# #         # Cetak angka 5
# #         print_number_5(size)
# #         # Cetak angka 4
# #         print_number_4(size)

# # # Ukuran angka
# # size = 7
# # print_number_154(size)









# # 154
# # Input for the size
# size = int(input("Masukan Size: "))

# # '1'
# i = 0
# while i < size:
#     if i == 0:
#         print("  X")
#     else:
#         print("  X")
#     i += 1
# print()

# # '5'
# i = 0
# while i < size:
#     if i == 0: 
#         print("XXXXX")
#     elif i < size // 2: 
#         print("X")
#     elif i == size // 2:  
#         print("XXXXX")
#     elif i < size - 1:  
#         print("    h") 
#     else:  
#         print("hhhhh") 
#     i += 1
# print()

# # '4'
# i = 0
# while i < size:
#     if i < size // 2:
#         print("X   X")
#     elif i == size // 2:
#         print("XXXXX")
#     else:
#         print("    X")
#     i += 1

# Input tinggi dari pengguna
tinggi = int(input("Masukkan tinggi: "))

# Angka 1
for baris in range(tinggi):
    # Cetak angka 1 di kolom tengah
    print(" " * (tinggi // 2) + "x")
print()

# Angka 5
for baris in range(tinggi):
    for kolom in range(tinggi):
        if baris == 0 or baris == tinggi // 2 or baris == tinggi - 1:  # Garis horizontal atas, tengah, dan bawah
            print("x", end="")
        elif baris < tinggi // 2 and kolom == 0:  # Garis vertikal kiri di bagian atas
            print("x", end="")
        elif baris > tinggi // 2 and kolom == tinggi - 1:  # Garis vertikal kanan di bagian bawah
            print("x", end="")
        else:
            print(" ", end="")
    print()
print()

# Angka 4
for baris in range(tinggi):
    for kolom in range(tinggi):
        if baris == tinggi // 2:  # Garis horizontal di tengah
            print("x", end="")
        elif kolom == tinggi - 1:  # Garis vertikal di kanan
            print("x", end="")
        elif baris < tinggi // 2 and kolom == 0:  # Garis vertikal kiri di atas
            print("x", end="")
        else:
            print(" ", end="")
    print()