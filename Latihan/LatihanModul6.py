# list = [1, "string", 2.5, True]
# print(list)
# del list[1]
# print(list)
# list.remove("string")
# print(len(list))
# list.append("buah")

# list.insert(1, "durian")
# print(list)

# anga = [1,3,4,6,3,2,6]

# print(max(angka))

# nama = ["agus", "bagas", "rafi", "ridho"]

# nama[2] = "messi"
# print(nama)

# for i in range(len(nama)) :
#     print(f"namaku adalah {nama[i]}")

#cobe tuple
# Tup1 = ('Pyhisics', 'Chemistry', 1997,2000)
# Tup2 = (0, 1, 2, 7)

# print (Tup1, Tup2)
# print(Tup1[2:5], Tup2[1:5])

# Buah = ("Apel" "apel", "manggis", "jambu","Gomu-gomu", )
# print("ini indeks pertama")







# data = []

# inventaris = (
#     ("papan tulis", "001")
#     ("pulpen hitam", "002")
#     ("Spidol","003")
# )

# def tambah_siswa():
#     print("\n-Tambah Data Siswa- ")
#     nama = input("masukkan Nama Siswa: ")
#     kelas = input("Masukkan Kelas Siswa: ")

#     data.append((nama, kelas))











#     def main():
#         while True :
#             print("Program pendataan mahasiswa")
#             print("1")



# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1,2,3,4,5,6,7];
# print ("Nilai list1[0]:",list1[0])
# print ("Nilai list2[1:5]:", list2[1:5])

# list = ['physics', 'chemistry', 1997, 2000];
# print ("Nilai indeks ke-2 saat ini :")
# print (list[2])
# list[2] = 2001;
# print ("Nilai indeks ke-2 setelah diperbaharui:")
# print (list[2])

# list1 = ['physics', 'chemistry', 1997,2000];
# print (list1)
# del list[2];
# print ("Setelah nilai indeks ke-2 dihapus:")
# print (list1)

# tup = ('physics,' 'chemistry', 1997, 2000);
# print (tup)
# del tup;
# print("Setelah tup dihapus:")
# print (tup)
# tup2 = (1,2,3,4,5,6,7);
# print ("tup1[0]:", tup1[0])
# print ("tup2[1:5]:", tup2[1:5])


# tup1 = (12, 34,56);
# tup2 = ('abc', 'xyz');
#sintaks seperti dibawah tidak bisa diterapkan di tuple
#tuple[0] = 100;
#Tuple hanya dapat mengambil isi dimasukkan ke Tuple baru
# tup3 = tup1 + tup2;
# print (tup3)

# warna = ['merah', 'biru', 'hijau']

# for i in warna:
#     for j in warna:
#         for k in warna:
#             for l in warna:
#                 print(f"Kombinasi:{i}, {j}, {k}, {l}")


A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

hasil = [[0,0],
         [0,0]]

for i in range(2): #baris matriks A
    for j  in range(2): #kolom matriks B
        for k in range(2):
            hasil[i][j] += A[i][k] * B[k][j]

for row in hasil:
    print(row)
    