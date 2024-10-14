#diminta untuk membuat kode menggambar angka atau Nim
size = int(input("Masukkan size: "))

# angka 0
for i in range(size):   # #i dan ii  variabel iterasi untuk baris (i) dan kolom (ii).
  for ii in range(size):
     if i == 0 or i == size - 1 or ii == 0 or ii == size - 1 :  # #if i == 0 or i == size - 1  baris pertama dan terakhir diisi karakter x, membentuk bagian atas dan bawah angka 0. #selanjutnya samping dan kiri
      print("x", end=" ") 
     else:
      print(" ", end=" ")
  print()
print()


# membuat angka 4
for i in range(size):
    for ii  in range(size): 
        if (ii == 0 and i <= size // 2) or (i == size // 2) or (ii == size - 1 and i >= size // 8): # ii == 0 and i <= size // 2 membuat garis vertikal di kolom pertama (ii == 0) dari baris pertama hingga baris tengah (i <= size // 2), yang merupakan bagian kiri angka 4. #i == size // 2 membuat garis horizontal di tengah (pada baris yang membagi ukuran menjadi dua).#ii == size - 1 and i >= size // 2 membuat garis vertikal di kolom terakhir (ii == size - 1) mulai dari setengah bawah (i >= size // 2), yang merupakan bagian kanan angka 4.
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")

# membuat angka 6
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size // 2 or i == size - 1 or ii == 0 or (ii == size - 1 and i >= size // 2): #i == 0 membuat garis horizontal di baris pertama,i == size // 2 membuat garis horizontal di baris tengah.,i == size - 1 membuat garis horizontal di baris terakhir,ii == 0 membuat garis vertikal di kolom pertama,ii == size - 1 and i >= size // 2 membuat garis vertikal di kolom terakhir 
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")


# h=t v=b