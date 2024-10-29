# Input ukuran dari user
size = int(input("Masukkan Size: "))
# Cetak angka 1 (pertama)
for i in range(size):
    if i < size:
        print(" " * ((size-1)//2) +"1")
print()  # Pindah baris

# Cetak angka 1 (kedua)
for i in range(size):
    if i < size:
       print(" " * ((size-1)//2) +"1")
print()  # Pindah baris

# #Cetak angka 4
for i in range(size):
    if i == size // 2:
        print("4" * size)
    elif i < size // 2:
        print("4" + " " * (size - 2) + "4")
    else:
        print(" " * (size-1) + "4")
