# def mencoba_fungsi ():
#   print("mencoba program fungsi")
# mencoba_fungsi()

# def masukkan_data():
#     nama = str (input("masukan nama: "))
#     NRP = int (input("masukkan NIM: "))
#     def cetak_string():
#       print("ini adalah fungsi mencetak string")
#       print("silahkan masukkan data")
#     cetak_string()
#     masukkan_data()

# def perkalian (a, b):
#     c = a * b
#     return c

# print(perkalian(5,10))

# f =  lambda x, y, z: x + y +z 
# print (f(10, 20, 30))

# z = (lambda a = "tic", b = "tac", c = "toe" : a + b + c)
# print(z("ZOO", "KUDA"))


def contohScope(X):
    X = 10
    print("Nilai X di dalam fungsi, X =", X)

X =30
print("Nilai X di luar fungsi, X =", X)
contohScope(X)

# volume_kubus = lambda sisi: sisi ** 3
# print("Volume kubus adalah:", volume_kubus(4))

# def hitung_todtal(angka):
#   total = angka +50
#   print("Nilai total di dalam fungsi:", total)

# total = 100
# print("Nilai total di luar fungsi:", total)

# hitung_total(30)

def ucapan():
  print("selamat malam")
ucapan()


